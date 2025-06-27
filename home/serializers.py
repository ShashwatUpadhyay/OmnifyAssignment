from rest_framework import serializers
from .models import FitnessClass, Booking
from django.utils import timezone
import pytz

# Function to convert datetime to the specified timezone

def convert_timezone(value, tz):
    if value and tz:
        local_tz = pytz.timezone(tz)
        return timezone.localtime(value, local_tz)
    return value

class FitnessClassSerializer(serializers.ModelSerializer):
    """
        Serializer for the FitnessClass model.
        This serializer includes a method to convert class_date and created_at to the specified timezone.
        It also calculates the number of available slots by subtracting the count of bookings from the total slots.
    """
    
    class Meta:
        model = FitnessClass
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['available_slots'] = instance.slots - instance.bookings.count()
        
        request = self.context.get('request', None)
        tz = request.GET.get('tz')
        if tz:
            try:
                data['class_date'] = convert_timezone(instance.class_date, tz)
                data['created_at'] = convert_timezone(instance.created_at, tz)
                data['time_zone'] = tz
            except pytz.UnknownTimeZoneError:
                data['class_date'] = instance.class_date
                data['created_at'] = instance.created_at
                data['time_zone'] = 'Asian/Kolkata'  # Default timezone if unknown. Already set in settings.py
                
        return data
    

class BookingCreateSerializer(serializers.ModelSerializer):
    """
        Serializer for creating a Booking instance.
        It validates that there are available slots for the class instance before allowing the booking to be created.
    """
    class_instance = serializers.PrimaryKeyRelatedField(queryset=FitnessClass.objects.all())
    
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, attrs):
        class_instance = attrs.get('class_instance')
        if class_instance.slots <= class_instance.bookings.count():
            raise serializers.ValidationError("No slots available for this class.") 
        return attrs

class BookingSerializer(serializers.ModelSerializer):
    """
        Serializer for the Booking model.
        This serializer includes all fields from the Booking model.
        It does not perform any additional validation or transformations.
    """
    class Meta:
        model = Booking
        fields = '__all__'