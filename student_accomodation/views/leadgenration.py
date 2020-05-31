from student_accomodation.serializers.leadgenrationserializers import LeadGenerationSerializer
from rest_framework import generics
from student_accomodation.models import LeadGeneration
from django.db.models import F

class list(generics.ListCreateAPIView):
    queryset = LeadGeneration.objects.all()
    serializer_class = LeadGenerationSerializer


class show(generics.RetrieveUpdateDestroyAPIView):
    queryset =LeadGeneration.objects.all()
    serializer_class = LeadGenerationSerializer