from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import FitnessClassViewSet, BookingCreateView,BookingsView

router = DefaultRouter()
router.register(r'classes', FitnessClassViewSet)

urlpatterns = [
    path('book/', BookingCreateView.as_view(), name='booking-create'),
    path('bookings/', BookingsView.as_view(), name='bookings-list'),
]

urlpatterns += router.urls
