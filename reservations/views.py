from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Hotel, Room, Customer, Reservation, Payment, Amenity
from .serializers import (
    HotelSerializer, RoomSerializer, CustomerSerializer,
    ReservationSerializer, PaymentSerializer, AmenitySerializer
)

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "location"]
    ordering_fields = ["name", "rating"]

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.select_related("hotel").all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["hotel", "room_type", "is_available"]
    search_fields = ["room_number", "room_type", "hotel__name", "hotel__location"]
    ordering_fields = ["price_per_night", "room_number"]

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["first_name", "last_name", "email"]
    ordering_fields = ["first_name", "last_name"]

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.select_related("customer", "room", "room__hotel").all()
    serializer_class = ReservationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["room", "customer", "check_in_date", "check_out_date"]
    search_fields = ["customer__first_name", "customer__last_name", "room__room_number", "room__hotel__name"]
    ordering_fields = ["check_in_date", "check_out_date", "total_price"]

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.select_related("reservation").all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["reservation", "method"]
    ordering_fields = ["amount", "paid_at"]

class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name"]
