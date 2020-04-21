from student_accomodation.models import Property,PropertyFacility,PropertyUniversity,University,Facility
# from student_accomodation.views import university
from rest_framework import serializers
from .stundent_manager import generate_slug


def create_property_facilty(facilities_list):
	#print(property_object,facilities_list,added_by_id)
	for facilities in facilities_list:
		facilities_array=facilities.split("-")
		facilities_id=int(facilities_array[0])
		facilities_type=facilities_array[1]
		yield facilities_id,facilities_type


class PropertySerializer(serializers.ModelSerializer):
	# university_slug=serializers.SerializerMethodField()
	# added_by_name=serializers.CharField(max_length=400,read_only=True)
	country_name=serializers.CharField(max_length=400,read_only=True)
	city_name=serializers.CharField(max_length=400,read_only=True)
	provider_name=serializers.CharField(max_length=400,read_only=True)
	facilities=serializers.CharField(max_length=2000,write_only=True)
	closest_universities=serializers.CharField(max_length=2000,write_only=True)
	currency_symbol=serializers.CharField(max_length=400,read_only=True)

	facilities_data=serializers.SerializerMethodField()


	# country_name=serializers.CharField(max_length=250,read_only=True)
	# added_by_name=serializers.CharField(max_length=250,read_only=True)
	class Meta:
		# fields = ('id','scale','banker_name','branch_detail','email','current_mobile','old_mobile_no1','old_mobile_no2','notes','marketer','level2_profile','level3_profile','is_deleted','bank','bank_name','bank','marketer_name','status','visiting_card','added_date','banker_mobile','firm','firm_name',)
		fields = '__all__'
		#exclude = ('status', )
		model = Property

	# def get_university_slug(self,obj):
	# 	return generate_slug(obj.name)
	def get_facilities_data(self,obj):
		dict1={}
		try:
			# dict1={}{}
			dict1['amenity']=[{"id":x.facilities.id,"title":x.facilities.title} for x in obj.property_facility.filter(facilities_category__iexact='amenities')]
			dict1['safetyAndSecurity']=[{"id":x.facilities.id,"title":x.facilities.title} for x in obj.property_facility.filter(facilities_category__iexact='safetyAndSecurity')]
			dict1['rentInclusions']=[{"id":x.facilities.id,"title":x.facilities.title} for x in obj.property_facility.filter(facilities_category__iexact='rentInclusions')]
			# list1=[]
			# for x in obj.property_facility.all():
			# 	if x.facilities_category not in dict1.keys():
			# 		dict1[x.facilities_category]={"id":x.facilities.id,"title":x.facilities.title}
			# # 	print(x.facilities.id)
			# 	else:
			# 		dict1[x.facilities_category].update({"id":x.facilities.id,"title":x.facilities.title})
			# 	list1.append(dict1)
			# 	dict1={}
				
			return dict1
		except Exception as e:
			print(e)
			return None
	def create(self,validated_data):
		university=eval(validated_data.pop('closest_universities'))
		facilities_data=eval(validated_data.pop('facilities'))
		amenities=list(map(lambda x:str(x)+"-amenities",facilities_data[0]['amenities']))
		safety_security=list(map(lambda x:str(x)+"-safetyAndSecurity",facilities_data[0]['safetyAndSecurity']))
		rent_inclusions=list(map(lambda x:str(x)+"-rentInclusions",facilities_data[0]['rentInclusions']))
		property_object=Property.objects.create(**validated_data)
		amenities.extend(safety_security)
		amenities.extend(rent_inclusions)
		
		for facility_detail in create_property_facilty(amenities):
			PropertyFacility.objects.create(property_detail=property_object,facilities=Facility.objects.get(id=facility_detail[0]),facilities_category=facility_detail[1],added_by=validated_data['added_by'])

		for university_id in university:
			PropertyUniversity.objects.create(property_detail=property_object,university=University.objects.get(id=university_id),added_by=validated_data['added_by']) 
				
		# PropertyFacility.objects.bulk_create([PropertyFacility(property_detail=property_object,facilities=,facilities_category=)])
		return property_object
	def update(self,instance,validated_data):
		university=eval(validated_data.pop('closest_universities'))
		facilities_data=eval(validated_data.pop('facilities'))
		amenities=list(map(lambda x:str(x)+"-amenities",facilities_data[0]['amenities']))
		safety_security=list(map(lambda x:str(x)+"-safetyAndSecurity",facilities_data[0]['safetyAndSecurity']))
		rent_inclusions=list(map(lambda x:str(x)+"-rentInclusions",facilities_data[0]['rentInclusions']))
		property_object=Property.objects.filter(id=instance.id).update(**validated_data)
		PropertyFacility.objects.filter(property_detail=instance.id).delete()
		amenities.extend(safety_security)
		amenities.extend(rent_inclusions)
		for facility_detail in create_property_facilty(amenities):
			obj,created =	PropertyFacility.objects.get_or_create(property_detail=instance,facilities=Facility.objects.get(id=facility_detail[0]),facilities_category=facility_detail[1],added_by=validated_data['added_by'])
			print(obj)
			print(created)
		for university_id in university:
			obj,created	=	PropertyUniversity.objects.get_or_create(property_detail=instance,university=University.objects.get(id=university_id),added_by=validated_data['added_by']) 
		
		return instance