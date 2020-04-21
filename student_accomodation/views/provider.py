from student_accomodation.serializers.providerserializers import ProviderSerializer
from rest_framework import generics
from student_accomodation.models import Provider
from django.db.models import F


class list(generics.ListCreateAPIView):
    queryset = Provider.objects.select_related('added_by').annotate(added_by_name=F('added_by__first_name')).filter(is_enabled=1).all()
    serializer_class = ProviderSerializer

    # def get_queryset(self):
    # 	queryset=Country.objects.select_related('added_by').filter(status=0).all()
    # 	queryset=queryset.annotate(added_by_name=F('added_by__first_name'))
    # 	return queryset


class show(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.select_related('added_by').annotate(added_by_name=F('added_by__first_name')).filter(is_enabled=1).all()
    serializer_class =ProviderSerializer