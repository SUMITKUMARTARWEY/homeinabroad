from rest_framework_simplejwt.views import TokenObtainPairView     
from .loginSerializers import MyTokenObtainPairSerializer
class LoginView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer
