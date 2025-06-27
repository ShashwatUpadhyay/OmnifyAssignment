from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FitnessClass(models.Model):
    class_name = models.CharField(max_length=100, unique=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='classes')
    class_date = models.DateTimeField()
    slots = models.PositiveIntegerField(default=20)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.class_name
    
class Booking(models.Model):
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    class_instance = models.ForeignKey(FitnessClass, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('client_name', 'class_instance')
    
    def __str__(self):
        return f"{self.client_name} - {self.class_instance.class_name}"