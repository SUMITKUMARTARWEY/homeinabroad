from student_accomodation.models import Provider,ProviderCity,City
from student_accomodation.views import university
from rest_framework import serializers
from .stundent_manager import generate_slug

class ProviderSerializer(serializers.ModelSerializer):
	provider_slug=serializers.SerializerMethodField()
	added_by_name=serializers.CharField(max_length=400,read_only=True)
	# country_name=serializers.CharField(max_length=400,read_only=True)
	# city_name=serializers.CharField(max_length=400,read_only=True)
	city_ids=serializers.CharField(max_length=400,write_only=True,allow_null=True,allow_blank=True)
	provider_city=serializers.SerializerMethodField()
	# country_name=serializers.CharField(max_length=250,read_only=True)
	# added_by_name=serializers.CharField(max_length=250,read_only=True)
	class Meta:
		# fields = ('id','scale','banker_name','branch_detail','email','current_mobile','old_mobile_no1','old_mobile_no2','notes','marketer','level2_profile','level3_profile','is_deleted','bank','bank_name','bank','marketer_name','status','visiting_card','added_date','banker_mobile','firm','firm_name',)
		fields = '__all__'
		#exclude = ('status', )
		model = Provider

	def get_provider_slug(self,obj):
		return generate_slug(obj.name)
	def get_provider_city(self,obj):
		try:
			return [{"city_id":x.city.id,"city_name":x.city.name} for x in obj.provider_city.all()]
		except:
			return None
	
	def create(self,validated_data):
		# print(validated_data['city_ids'])
		city_ids=eval(validated_data.pop('city_ids'))
		print(type(city_ids))
		print(validated_data)
		provider_object=Provider.objects.create(**validated_data)
		for city_id in city_ids:
			ProviderCity.objects.create(provider=provider_object,city=City.objects.get(id=city_id),added_by=validated_data['added_by'])
		# print(self.context.get('view').request.POST)
		return provider_object

	def update(self,instance,validated_data):
		print(instance)
		print(validated_data)
		city_ids=eval(validated_data.pop('city_ids'))
		print(type(city_ids))
		print(validated_data)
		provider_object=Provider.objects.filter(id=instance.id).update(**validated_data)
		ProviderCity.objects.filter(provider=instance.id).delete()
		for city_id in city_ids:
				ProviderCity.objects.create(provider=instance,city=City.objects.get(id=city_id),added_by=validated_data['added_by'])
		# print(self.context.get('view').request.POST)
		return instance