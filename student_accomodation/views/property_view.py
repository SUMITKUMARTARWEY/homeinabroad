from student_accomodation.serializers.propertyserializers import PropertySerializer,PropertyWebsiteSerializer,PropertySearchSerializer
from student_accomodation.serializers.cityserializers import  CitySearchSerializer
from student_accomodation.serializers.universityserializers import UniversitySearchSerializer
from rest_framework import generics
from student_accomodation.models import Property,City,University
from django.db.models import F
from rest_framework.views import APIView
from rest_framework.response import Response
class list(generics.ListCreateAPIView):
    queryset = Property.objects.select_related('added_by','city','country','provider').annotate(added_by_name=F('added_by__first_name'),city_name=F('city__name'),country_name=F('country__name'),provider_name=F('provider__name'),currency_symbol=F('country__currency_symbol')).filter(is_enabled=1).all()
    serializer_class = PropertySerializer


class show(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.select_related('added_by','city','country','provider').annotate(added_by_name=F('added_by__first_name'),city_name=F('city__name'),country_name=F('country__name'),provider_name=F('provider__name'),currency_symbol=F('country__currency_symbol')).filter(is_enabled=1).all()
    serializer_class = PropertySerializer

class search_detail(APIView):
    def get(self,request):
        if request.method == 'GET':
            search=self.request.query_params.get('search',None)
            if len(search)>0:
                property_queryset = Property.objects.select_related('added_by','city','country','provider').filter(is_enabled=1).all()
                property_serializer = PropertySearchSerializer(property_queryset,many=True)
            # print(property_serializer.data)
                city_queryset=City.objects.all()
                city_serializer = CitySearchSerializer(city_queryset,many=True)
                dict1=city_serializer.data
                university_queryset=University.objects.select_related('added_by').all()
                university_serializer=UniversitySearchSerializer(university_queryset,many=True)
                dict2=university_serializer.data
                # print(list(dict2))
                # print(list(dict1))
            # search_data=country_serializer.data.extends(property_serializer.data)
            # print(search_data)
            # search_data.extends(country_serializer.data)
                return Response((dict1.extend(dict2)))

    # print(queryset)
class property_website_list(generics.ListCreateAPIView):
    queryset = Property.objects.select_related('added_by','city','country','provider').annotate(added_by_name=F('added_by__first_name'),city_name=F('city__name'),country_name=F('country__name'),provider_name=F('provider__name'),currency_symbol=F('country__currency_symbol')).filter(is_enabled=1).all()
    serializer_class = PropertyWebsiteSerializer

    def get_queryset(self):
        queryset=Property.objects.select_related('added_by','city','country','provider').annotate(added_by_name=F('added_by__first_name'),city_name=F('city__name'),country_name=F('country__name'),provider_name=F('provider__name'),currency_symbol=F('country__currency_symbol')).filter(is_enabled=1).all()
        property_slug=self.request.query_params.get('property_slug',None)

        if property_slug is not None:
            queryset=queryset.filter(property_slug__iexact=property_slug)
        # if ranking is not None:
        #     queryset=queryset.order_by('+ranking')

        return queryset