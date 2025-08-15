from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, RoomViewSet, CustomerViewSet, ReservationViewSet, PaymentViewSet, AmenityViewSet

router = DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'amenities', AmenityViewSet)

urlpatterns = router.urls
