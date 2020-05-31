from student_accomodation.serializers.contactusserializers import ContactUsSerializer
from rest_framework import generics
from student_accomodation.models import ContactUs
from django.db.models import F


class list(generics.ListCreateAPIView):
    queryset = ContactUs.objects.filter(is_enabled=1).all()
    serializer_class = ContactUsSerializer

class show(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactUs.objects.filter(is_enabled=1).all()
    serializer_class = ContactUsSerializer