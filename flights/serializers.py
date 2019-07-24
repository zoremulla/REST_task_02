from rest_framework import serializers

from .models import Flight, Booking


class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ['destination', 'time', 'price', 'id']


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'id']


class Booking_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'flight', 'date', 'passengers']

class Booking_updateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Booking
        fields= ['passengers', 'date']
