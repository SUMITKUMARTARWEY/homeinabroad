from student_accomodation.serializers.cityserializers import CitySerializer
from rest_framework import generics
from student_accomodation.models import City
from django.db.models import F


class list(generics.ListCreateAPIView):
    queryset = City.objects.select_related('added_by').annotate(added_by_name=F('added_by__first_name'),country_name=F('country__name')).filter(is_enabled=1).all()
    serializer_class = CitySerializer

class show(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.select_related('added_by').annotate(added_by_name=F('added_by__first_name'),country_name=F('country__name')).filter(is_enabled=1).filter(is_enabled=1).all()
    serializer_class = CitySerializer