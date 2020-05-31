from student_accomodation.models import Country
# from student_accomodation.views import country
from rest_framework import serializers
from .stundent_manager import generate_slug
class CountrySerializer(serializers.ModelSerializer):
	country_slug=serializers.SerializerMethodField()
	added_by_name=serializers.CharField(max_length=400,read_only=True)
	currnecy_name=serializers.CharField(max_length=400,read_only=True)
	# city_name=serializers.CharField(max_length=150,write_only=True)
	# added_by_name=serializers.CharField(max_length=250,read_only=True)
	# password=serializers.CharField(write_only=True,allow_null=True)
	class Meta:
		# fields = ('id','scale','banker_name','branch_detail','email','current_mobile','old_mobile_no1','old_mobile_no2','notes','marketer','level2_profile','level3_profile','is_deleted','bank','bank_name','bank','marketer_name','status','visiting_card','added_date','banker_mobile','firm','firm_name',)
		fields = '__all__'
		#exclude = ('status', );;
		model = Country

	def get_country_slug(self,obj):
		return generate_slug(obj.name)


	# def create(self,validated_data):
	# 	city_name=validated_data.pop('city_name')
	# 	country=Country.objects.create(**validated_data)
	# 	city=City.objects.create(city_name=city_name,country=country,added_by=validated_data['added_by'])
	# 	return country