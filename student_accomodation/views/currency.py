from student_accomodation.serializers.currencyserializers import CurrencySerializer
from rest_framework import generics
from student_accomodation.models import Currency
from django.db.models import F

class list(generics.ListCreateAPIView):
    queryset = Currency.objects.select_related('added_by').annotate(added_by_name=F('added_by__first_name')).all()
    serializer_class = CurrencySerializer

    # def get_queryset(self):
    # 	queryset=Country.objects.select_related('added_by').filter(status=0).all()
    # 	queryset=queryset.annotate(added_by_name=F('added_by__first_name'))
    # 	return queryset


class show(generics.RetrieveUpdateDestroyAPIView):
    queryset = Currency.objects.select_related('added_by').annotate(added_by_name=F('added_by__first_name')).all()
    serializer_class = CurrencySerializer