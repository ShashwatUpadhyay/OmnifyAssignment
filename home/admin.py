from django.contrib import admin
from .models import *
# Register your models here.
class FitnessClassAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'instructor', 'class_date', 'slots', 'created_at')
    search_fields = ('class_name', 'instructor__username')
    list_filter = ('class_date',)
    
class BookingAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_email', 'class_instance', 'booking_date')
    search_fields = ('client_name__username', 'class_instance__class_name')
    list_filter = ('booking_date',)
    
admin.site.register(FitnessClass,FitnessClassAdmin)
admin.site.register(Booking,BookingAdmin)
