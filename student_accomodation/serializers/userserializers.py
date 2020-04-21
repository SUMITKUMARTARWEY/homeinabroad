from student_accomodation.views import user
from rest_framework import serializers
from django.contrib.auth.models import User
# from datetime import datetime

class UserSerializer(serializers.ModelSerializer):
	# password=serializers.CharField(write_only=True,allow_null=True)
	# added_by_name=serializers.CharField(max_length=250,read_only=True)
	class Meta:
		# fields = ('id','scale','banker_name','branch_detail','email','current_mobile','old_mobile_no1','old_mobile_no2','notes','marketer','level2_profile','level3_profile','is_deleted','bank','bank_name','bank','marketer_name','status','visiting_card','added_date','banker_mobile','firm','firm_name',)
		
		exclude = ('is_superuser','is_staff','user_permissions','groups')
		model = User
		extra_kwargs = {
            'password': {'write_only': True}
        }


# 	def create(self,validated_data):
# 		# print(validated_data)
# 		password=validated_data.pop('password')
# 		user=User.objects.create_user(username=validated_data['email'],email=validated_data['email'],password=password
# ,first_name=validated_data['first_name'],last_name=validated_data['last_name'],is_active=1,date_joined=datetime.now())
# 		validated_data['auth_user']=user
# 		user_create=Users.objects.create(**validated_data)
# 		return user_create
# 	def update(self,instance,validated_data):
# 		# print(validated_data)
# 		password= validated_data.pop('password') if 'password' in validated_data else None
# 		auth_user_intance=instance.auth_user
# 		auth_user_intance.username=validated_data['email']
# 		auth_user_intance.email=validated_data['email']
# 		auth_user_intance.first_name=validated_data['first_name']
# 		auth_user_intance.last_name=validated_data['last_name']
# 		auth_user_intance.save()
# 		instance.email=validated_data.get('email',instance.email)
# 		instance.first_name=validated_data.get('first_name',instance.first_name)
# 		instance.last_name=validated_data.get('last_name',instance.last_name)
# 		instance.contant_no=validated_data.get('contant_no',instance.contant_no)
# 		instance.save()
# 		return instance