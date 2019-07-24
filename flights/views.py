from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from datetime import datetime
from django.http import JsonResponse
from .models import Flight, Booking
from .serializers import FlightSerializer, BookingSerializer, Booking_updateSerializer, Booking_detailSerializer


class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class BookingsList(ListAPIView):
	queryset = Booking.objects.filter(date__gte=datetime.today())
	serializer_class = BookingSerializer


class Bookingdetail(RetrieveAPIView):
    queryset= Booking.objects.all()
    serializer_class= Booking_detailSerializer
    look_field= 'id'
    lookup_url_kwarg= 'booking_id'

class Updatebooking(RetrieveUpdateAPIView):
    queryset=Booking.objects.all()
    serializer_class= Booking_updateSerializer
    look_field= 'id'
    lookup_url_kwarg= 'booking_id'


class Cancelbooking(DestroyAPIView):
    queryset=Booking.objects.all()
    #we dont need a serializer because we are destroying and not retrieving any info
    look_field= 'id'
    lookup_url_kwarg= 'booking_id'