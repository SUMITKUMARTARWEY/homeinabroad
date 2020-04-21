from student_accomodation.serializers.propertyserializers import PropertySerializer
from rest_framework import generics
from student_accomodation.models import Property
from django.db.models import F

class list(generics.ListCreateAPIView):
    queryset = Property.objects.select_related('added_by','city','country','provider').annotate(added_by_name=F('added_by__first_name'),city_name=F('city__name'),country_name=F('country__name'),provider_name=F('provider__name'),currency_symbol=F('country__currency_symbol')).filter(is_enabled=1).all()
    serializer_class = PropertySerializer


class show(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.select_related('added_by','city','country','provider').annotate(added_by_name=F('added_by__first_name'),city_name=F('city__name'),country_name=F('country__name'),provider_name=F('provider__name'),currency_symbol=F('country__currency_symbol')).filter(is_enabled=1).all()
    serializer_class = PropertySerializer