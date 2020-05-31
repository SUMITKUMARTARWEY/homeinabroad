from student_accomodation.serializers.bookingserializers import BookingSerializer
from rest_framework import generics
from student_accomodation.models import Booking
from django.db.models import F


class list(generics.ListCreateAPIView):
    queryset = Booking.objects.filter(is_enabled=1).all()
    serializer_class = BookingSerializer

class show(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.filter(is_enabled=1).all()
    serializer_class = BookingSerializer