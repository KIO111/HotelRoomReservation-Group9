from django.db import models
from django.core.exceptions import ValidationError

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)

    def __str__(self):
        return f"{self.name} - {self.location}"


class Amenity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Room(models.Model):
    ROOM_TYPES = [
        ("single", "Single"),
        ("double", "Double"),
        ("suite", "Suite"),
    ]

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms")
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    amenities = models.ManyToManyField(Amenity, blank=True)

    def __str__(self):
        return f"Room {self.room_number} - {self.hotel.name}"


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def clean(self):
        if self.check_out_date <= self.check_in_date:
            raise ValidationError("Check-out date must be after check-in date.")

        # Prevent overlapping bookings
        overlapping = Reservation.objects.filter(
            room=self.room,
            check_in_date__lt=self.check_out_date,
            check_out_date__gt=self.check_in_date
        ).exclude(id=self.id)
        if overlapping.exists():
            raise ValidationError("Room is already booked for these dates.")

    def save(self, *args, **kwargs):
        self.clean()
        nights = (self.check_out_date - self.check_in_date).days
        self.total_price = self.room.price_per_night * nights
        super().save(*args, **kwargs)

        # Mark room as unavailable
        self.room.is_available = False
        self.room.save()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        # Mark room as available again
        self.room.is_available = True
        self.room.save()

    def __str__(self):
        return f"Reservation for {self.customer} in {self.room}"


class Payment(models.Model):
    METHODS = [
        ("cash", "Cash"),
        ("credit_card", "Credit Card"),
        ("mobile_money", "Mobile Money"),
    ]

    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=METHODS)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} for {self.reservation}"
