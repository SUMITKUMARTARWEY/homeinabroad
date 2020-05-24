from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self,attr):
        data=super().validate(attr)
        # print(data)
        token=self.get_token(self.user)
        data['user']=self.user.id
        return data

