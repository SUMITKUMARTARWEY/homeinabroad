from student_accomodation.serializers.requestserviceserializers import RequestServiceSerializer
from rest_framework import generics
from student_accomodation.models import RequestService
from django.db.models import F
class list(generics.ListCreateAPIView):
    queryset = RequestService.objects.filter(is_enabled=1).all()
    serializer_class = RequestServiceSerializer

    # def get_queryset(self):
    #   queryset=Country.objects.select_related('added_by').filter(status=0).all()
    #   queryset=queryset.annotate(added_by_name=F('added_by__first_name'))
    #   return queryset


class show(generics.RetrieveUpdateDestroyAPIView):
    queryset = RequestService.objects.filter(is_enabled=1).all()
    serializer_class = RequestServiceSerializer