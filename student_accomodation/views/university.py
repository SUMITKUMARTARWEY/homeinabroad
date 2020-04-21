from student_accomodation.serializers.universityserializers import UniversitySerializer
from rest_framework import generics
from student_accomodation.models import University
from django.db.models import F
class list(generics.ListCreateAPIView):
    queryset = University.objects.select_related('added_by','country','city').annotate(added_by_name=F('added_by__first_name'),country_name=F('country__name'),city_name=F('city__name')).filter(is_enabled=1).all()
    serializer_class = UniversitySerializer

    # def get_queryset(self):
    # 	queryset=Country.objects.select_related('added_by').filter(status=0).all()
    # 	queryset=queryset.annotate(added_by_name=F('added_by__first_name'))
    # 	return queryset


class show(generics.RetrieveUpdateDestroyAPIView):
    queryset = University.objects.select_related('added_by','country','city').annotate(added_by_name=F('added_by__first_name'),country_name=F('country__name'),city_name=F('city__name')).filter(is_enabled=1).all()
    serializer_class = UniversitySerializer