from django.shortcuts import render
from rest_framework import viewsets
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer,BookingCreateSerializer,BookingSerializer
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class FitnessClassViewSet(viewsets.ModelViewSet):
    """    
        This viewset provides a list of fitness classes that are scheduled for the future.
        It uses the FitnessClassSerializer to serialize the data.
        The queryset filters classes to only include those with a class_date greater than or equal to the current date and time.
    """
    
    queryset = FitnessClass.objects.filter(class_date__gte=datetime.now()).order_by('class_date')
    serializer_class = FitnessClassSerializer
    http_method_names = ['get']
    
    
class BookingCreateView(APIView):
    """
        This view handles the booking of fitness classes.
        It uses the BookingCreateSerializer to validate and save the booking data.
        If the booking is successful, it returns a success message with the booking data.   
        If the booking fails, it returns an error message with the validation errors.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Your class is booked!", "data": serializer.data}, status=201)
        else:
            return Response({"message":"Booking Failed", "error": serializer.errors}, status=400)
        
class BookingsView(APIView):
    """
        This view retrieves bookings based on the client's email.
        It uses the BookingCreateSerializer to serialize the booking data.
        If the email parameter is provided, it filters bookings by client_email and returns the data.
        If the email parameter is missing, it returns an error message.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def get(self, request):
        """
            Retrieves bookings based on the client's email.
            Expects an 'email' parameter in the GET request.
        """
        email = request.GET.get('email', None)
        if email is not None:
            bookings = Booking.objects.filter(client_email=email)
            serializer = self.serializer_class(bookings, many=True)
            return Response({"message":"Booking Fetched!", "data": serializer.data}, status=200)
        else:
            return Response({"error": "Email parameter is required."}, status=400)