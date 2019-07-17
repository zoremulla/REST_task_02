from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import date

from .models import Flight, Booking


class FlightListTest(APITestCase):
	def setUp(self):
		self.flight1 = {'destination': 'Wakanda', 'time': '10:00', 'price': 230, 'miles': 4000}
		self.flight2 = {'destination': 'La la land', 'time': '00:00', 'price': 1010, 'miles': 1010}
		Flight.objects.create(**self.flight1)
		Flight.objects.create(**self.flight2)

	def test_url_works(self):
		response = self.client.get(reverse('flights-list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)


	def test_list(self):
		response = self.client.get(reverse('flights-list'))
		flights = Flight.objects.all()
		self.assertEqual(len(response.data), flights.count())
		flight = flights[0]
		self.assertEqual(dict(response.data[0]), {"id" : flight.id, "destination" : flight.destination, "time": str(flight.time), "price": str(flight.price)})
		flight = flights[1]
		self.assertEqual(dict(response.data[1]), {"id" : flight.id, "destination" : flight.destination, "time": str(flight.time), "price": str(flight.price)})


class BookingListTest(APITestCase):
	def setUp(self):
		self.flight1 = {'destination': 'Wakanda', 'time': '10:00', 'price': 230, 'miles': 4000}
		self.flight2 = {'destination': 'La la land', 'time': '00:00', 'price': 1010, 'miles': 1010}
		flight1 = Flight.objects.create(**self.flight1)
		flight2 = Flight.objects.create(**self.flight2)
		user = User.objects.create(username="laila", password="1234567890-=")

		Booking.objects.create(flight=flight1, date="2018-01-01", user=user, passengers=2)
		Booking.objects.create(flight=flight2, date="2019-01-01", user=user, passengers=2)
		Booking.objects.create(flight=flight1, date="2020-01-01", user=user, passengers=2)
		Booking.objects.create(flight=flight2, date="2021-01-01", user=user, passengers=2)


	def test_url_works(self):
		response = self.client.get(reverse('bookings-list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)


	def test_response(self):
		response = self.client.get(reverse('bookings-list'))
		bookings = Booking.objects.filter(date__gt=date.today())

		self.assertEqual(len(response.data), bookings.count())
		booking = bookings[0]
		self.assertEqual(dict(response.data[0]), {"id" : booking.id, "flight" : booking.flight.id, "date": str(booking.date)})
		booking = bookings[1]
		self.assertEqual(dict(response.data[1]), {"id" : booking.id, "flight" : booking.flight.id, "date": str(booking.date)})


class BookingDetails(APITestCase):
	def setUp(self):
		flight1 = {'destination': 'Wakanda', 'time': '10:00', 'price': 230, 'miles': 4000}
		flight2 = {'destination': 'La la land', 'time': '00:00', 'price': 1010, 'miles': 1010}

		flight1 = Flight.objects.create(**flight1)
		flight2 = Flight.objects.create(**flight2)
		user = User.objects.create(username="laila", password="1234567890-=")

		Booking.objects.create(flight=flight1, date="2018-01-01", user=user, passengers=2)
		Booking.objects.create(flight=flight2, date="2019-01-01", user=user, passengers=2)
		Booking.objects.create(flight=flight1, date="2020-01-01", user=user, passengers=2)
		Booking.objects.create(flight=flight2, date="2021-01-01", user=user, passengers=2)

	def test_url_works(self):
		response = self.client.get(reverse('booking-details', args=[1]))
		self.assertEqual(response.status_code, status.HTTP_200_OK)


	def test_response(self):
		response = self.client.get(reverse('booking-details', args=[1]))
		booking = Booking.objects.get(id=1)
		self.assertEqual(dict(response.data), {"id" : booking.id, "flight" : booking.flight.id, "date": str(booking.date), "passengers":booking.passengers})

		response = self.client.get(reverse('booking-details', args=[2]))
		booking = Booking.objects.get(id=2)
		self.assertEqual(dict(response.data), {"id" : booking.id, "flight" : booking.flight.id, "date": str(booking.date), "passengers":booking.passengers})



class BookingUpdate(APITestCase):
	def setUp(self):
		flight1 = {'destination': 'Wakanda', 'time': '10:00', 'price': 230, 'miles': 4000}
		flight2 = {'destination': 'La la land', 'time': '00:00', 'price': 1010, 'miles': 1010}

		flight1 = Flight.objects.create(**flight1)
		flight2 = Flight.objects.create(**flight2)
		user = User.objects.create(username="laila", password="1234567890-=")

		Booking.objects.create(flight=flight1, date="2018-01-01", user=user, passengers=2)
		Booking.objects.create(flight=flight2, date="2019-01-01", user=user, passengers=2)
		Booking.objects.create(flight=flight1, date="2020-01-01", user=user, passengers=2)
		Booking.objects.create(flight=flight2, date="2021-01-01", user=user, passengers=2)

	def test_url_works(self):
		data = {"date": "2019-05-05", "passengers": 4}
		response = self.client.put(reverse('update-booking', args=[1]), data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)


	def test_update(self):
		data = {"date": "2019-05-05", "passengers": 4}

		old_booking = Booking.objects.get(id=1)
		response = self.client.put(reverse('update-booking', args=[1]), data)
		new_booking = Booking.objects.get(id=1)
		self.assertEqual({"id":old_booking.id, "date":data["date"], "passengers":data["passengers"], "flight":old_booking.flight, "user":old_booking.user}, {"id":new_booking.id, "date":str(new_booking.date), "passengers":new_booking.passengers, "flight":new_booking.flight, "user":new_booking.user})


		old_booking = Booking.objects.get(id=2)
		response = self.client.put(reverse('update-booking', args=[2]), data)
		new_booking = Booking.objects.get(id=2)
		self.assertEqual({"id":old_booking.id, "date":data["date"], "passengers":data["passengers"], "flight":old_booking.flight, "user":old_booking.user}, {"id":new_booking.id, "date":str(new_booking.date), "passengers":new_booking.passengers, "flight":new_booking.flight, "user":new_booking.user})
		

class BookingDelete(APITestCase):
	def setUp(self):
		flight1 = {'destination': 'Wakanda', 'time': '10:00', 'price': 230, 'miles': 4000}
		flight2 = {'destination': 'La la land', 'time': '00:00', 'price': 1010, 'miles': 1010}

		flight1 = Flight.objects.create(**flight1)
		flight2 = Flight.objects.create(**flight2)
		user = User.objects.create(username="laila", password="1234567890-=")

		Booking.objects.create(flight=flight1, date="2018-01-01", user=user, passengers=2)
		Booking.objects.create(flight=flight2, date="2019-01-01", user=user, passengers=2)
		Booking.objects.create(flight=flight1, date="2020-01-01", user=user, passengers=2)
		Booking.objects.create(flight=flight2, date="2021-01-01", user=user, passengers=2)

	def test_url_works(self):
		response = self.client.delete(reverse('cancel-booking', args=[1]))
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


	def test_update(self):
		response = self.client.delete(reverse('cancel-booking', args=[1]))
		self.assertEqual(Booking.objects.all().count(), 3)
		self.assertEqual(Booking.objects.filter(id=1).count(), 0)


