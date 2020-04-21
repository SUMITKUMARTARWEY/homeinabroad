from student_accomodation.serializers.userserializers import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User


class list(generics.ListCreateAPIView):
    queryset = User.objects.filter(is_active=True).all()
    serializer_class = UserSerializer


class show(generics.RetrieveUpdateDestroyAPIView):
    queryset =  User.objects.filter(is_active=True).all()
    serializer_class = UserSerializer