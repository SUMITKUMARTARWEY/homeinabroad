from student_accomodation.serializers.facilityserializers import FacilitySerializer
from rest_framework import generics
from student_accomodation.models import Facility
from django.db.models import F

class list(generics.ListCreateAPIView):
    queryset = Facility.objects.select_related('added_by').annotate(added_by_name=F('added_by__first_name')).filter(is_enabled=1).filter().all()
    serializer_class = FacilitySerializer


class show(generics.RetrieveUpdateDestroyAPIView):
    queryset =Facility.objects.select_related('added_by').annotate(added_by_name=F('added_by__first_name')).filter(is_enabled=1).all()
    serializer_class = FacilitySerializer