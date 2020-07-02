from student_accomodation.serializers.cityserializers import CitySerializer
from rest_framework import generics
from student_accomodation.models import City
from django.db.models import F


class list(generics.ListCreateAPIView):
    queryset = City.objects.select_related('added_by').annotate(added_by_name=F('added_by__first_name'),country_name=F('country__name')).filter(is_enabled=1).all()
    serializer_class = CitySerializer


    def get_queryset(self):
        print(args)
        print(kwargs)
        queryset=City.objects.select_related('added_by').annotate(added_by_name=F('added_by__first_name'),country_name=F('country__name')).filter(is_enabled=1).all()
        city_ranking=self.request.query_params.get('city_ranking',None)
        if city_ranking is not None:
            # print(city_ranking)
            # city_ranking_order=city_ranking+'city_ranking'
            queryset=queryset.order_by('city_ranking') 
        return queryset

class show(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.select_related('added_by').annotate(added_by_name=F('added_by__first_name'),country_name=F('country__name')).filter(is_enabled=1).filter(is_enabled=1).all()
    serializer_class = CitySerializer

class city_detail(show):
    lookup_field='city_slug'