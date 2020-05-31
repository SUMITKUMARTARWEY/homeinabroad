from student_accomodation.serializers.enquiryserializers import EnquirySerializer
from rest_framework import generics
from student_accomodation.models import Enquiry
from django.db.models import F


class list(generics.ListCreateAPIView):
    queryset = Enquiry.objects.filter(is_enabled=1).all()
    serializer_class = EnquirySerializer

class show(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enquiry.objects.filter(is_enabled=1).all()
    serializer_class = EnquirySerializer