from django.contrib import admin
from .models import Hotel, Room, Customer, Reservation, Payment, Amenity

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Customer)
admin.site.register(Reservation)
admin.site.register(Payment)
admin.site.register(Amenity)
