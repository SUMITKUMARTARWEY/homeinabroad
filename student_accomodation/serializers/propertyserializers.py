from student_accomodation.models import Property,PropertyFacility,PropertyUniversity,University,Facility,PropertyOffers,RoomCategory,RoomCategoryOffer,RoomType,BedPricing,RoomTypeOffer	
# from student_accomodation.views import university
from rest_framework import serializers
from .stundent_manager import generate_slug
import json

class PropertyOfferSerializers(serializers.ModelSerializer):
	def __init__(self, *args, **kwargs):
		# print(kwargs)
		# print(args)
        # many = kwargs.pop('many', True)
		super(PropertyOfferSerializers, self).__init__(many=True, *args, **kwargs)

	class Meta:

		fields = '__all__'
		#exclude = ('status', )
		model = PropertyOffers


	def create(self, validated_data):
		# print("eenkhbhkhrek")
		# print(validated_data)
		offer_object=PropertyOffers.objects.create(**validated_data)
		return offer_object

# class RoomCategorySerializers(serializers.serializers):

	# def __init__(self, *args, **kwargs):
		# print(kwargs)
		# print(args)
        # many = kwargs.pop('many', True)
		# super(RoomCategorySerializers, self).__init__(many=True, *args, **kwargs)

	# class Meta:

	# 	fields = '__all__'
	# 	#exclude = ('status', )
	# 	model = RoomCategory


	# def create(self, validated_data):
	# 	# print("eenkhbhkhrek")
	# 	# print(self.context.get('view').request.data)
	# 	# offer_object=PropertyOffers.objects.create(**validated_data)
	# 	return offer_object


def create_category_type(validated_dict,propert_id):
	

	validated_dicted=json.loads(validated_dict)
	for category_data in (validated_dicted):
		# sprint(category_data)
		roomcategory=RoomCategory.objects.create(property_detail=propert_id,category_name=category_data['category_name'],category_description=category_data['category_description'],category_banner_imageurl=category_data['category_banner_imageurl'])
		# for offer in category_data['categoryOffer']:
		if len(category_data['categoryOffer']['offerTitle'])>0:
			RoomCategoryOffer.objects.create(roomcategory=roomcategory,title=category_data['categoryOffer']['offerTitle'],message=category_data['categoryOffer']['offerDescription'],validity_date=category_data['categoryOffer']['offerValidityDate'])
		for room_type in  category_data['roomTypes']:
			room_type_object=RoomType.objects.create(roomcategory=roomcategory,title=room_type['typeName'],type_area=room_type['typeArea'],type_description=room_type['typeDescription'],images=room_type['typeImages'])
			for room_offer in room_type['typeOffers']:
				RoomTypeOffer.objects.create(roomtype=room_type_object,title=room_offer['offerTitle'],message=room_offer['offerDescription'],validity_date=room_offer['offerValidityDate'])
			for bed_pricing in room_type['bedPricing']:
				BedPricing.objects.create(roomtype=room_type_object,is_shortterm=bed_pricing['isShortTerm'],hasnominatedbeds=bed_pricing['hasNominatedBeds'],numberofnominatedbeds=bed_pricing['numberOfNominatedBeds'],bedavailabilitystatus=bed_pricing['bedAvailabilityStatus'],rentbreakup_duration=bed_pricing['rentBreakupDuration'],tenancy_durationunit=bed_pricing['tenancyDurationUnit'],room_checkin_date=bed_pricing['roomCheckInDate'],room_checkout_date=bed_pricing['roomCheckOutDate'],bed_price=bed_pricing['bedPrice'],bed_discounted_price=bed_pricing['bedDiscountedPrice'],deposit_charge=bed_pricing['depositCharge'],service_fee=bed_pricing['serviceFee'],taxes_inclusive=bed_pricing['taxesInclusive'],display_price_bed=bed_pricing['displayPriceOfBed'],display_discount_price_bed=bed_pricing['displayDiscountedPriceOfBed'],tenancy_duration=tenancy_duration['tenancyDuration'])    
		return roomcategory         
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
	# closest_universities
	near_by_university=serializers.SerializerMethodField()
	property_offers=PropertyOfferSerializers(source='property_offer',many=True,read_only=True)
	roomcategory=serializers.SerializerMethodField()
	country_slug=serializers.SerializerMethodField()
	city_slug=serializers.SerializerMethodField()
	# property_slug=serializers.SerializerMethodField()


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
			return dict1
		except Exception as e:
			# print(e)
			return None
	def get_near_by_university(self,obj):
		try:
			return [{"university_name":x.university.name,"university_id":x.university.id} for x in obj.property_university.all()]
		except:
			return None
	def get_roomcategory(self,obj):
		try:
			return [{"category_name":x.category_name,"category_description":x.category_description,"category_banner_imageurl":x.category_banner_imageurl,"category_offer":[{"title":y.title,"message":y.message,"validity_date":y.validity_date} for y in x.roomcategory.all()],"roomtype": [{"title":z.title,"type_area":z.type_area,"images":z.images,"type_description":z.type_description,"roomtype_offer":[{"title":w.title,"validity_date":w.validity_date,"message":w.message} for w in z.room_type_offer.all()],"bed_pricing":[{"is_shortterm":s.is_shortterm,"hasnominatedbeds":s.hasnominatedbeds,"bedavailabilitystatus":s.bedavailabilitystatus,"rentbreakup_duration":s.rentbreakup_duration,"tenancy_duration":s.tenancy_duration,"tenancy_durationunit":s.tenancy_durationunit,"room_checkin_date":s.room_checkin_date,"room_checkout_date":s.room_checkout_date,"bed_price":s.bed_price,"bed_discounted_price":s.bed_discounted_price,"deposit_charge":s.deposit_charge,"service_fee":s.service_fee,"taxes_inclusive":s.taxes_inclusive,"display_discount_price_bed":s.display_discount_price_bed,"display_price_bed":s.display_price_bed} for s in z.roomtype_bed_pricing.all() ]} for z in  x.room_type_category.all()]} for x in obj.property_category.all()]
		except Exception as e:
			# print(e)
			return None
	def get_country_slug(self,obj):
		try:
			return generate_slug(obj.country.name)
		except:
			return None
	def get_city_slug(self,obj):
		try:
			return generate_slug(obj.city.name)
		except:
			return None
	# s

	def create(self,validated_data):
		# validated_data['slug']=(validated_data['name'])
		# print(self.context.get('view').request.data)
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
		
		property_offers=[{'property_detail':property_object.id, **item} for item in json.loads(self.context.get('view').request.data['property_offers'])]
		# print(property_offers)
		property_offer_serializer=PropertyOfferSerializers(data=property_offers,many=True)
		if property_offer_serializer.is_valid():
			property_offer_serializer.save()
		# sprint(self.context.get('view').request.data['room_categories'])
		# print(eval(self.context.get('view').request.data['room_categories']))
		room_category_offer=create_category_type(self.context.get('view').request.data['room_categories'],property_object)
		return property_object

	def update(self,instance,validated_data):
		# validated_data['slug']=(validated_data['name'])
		university=eval(validated_data.pop('closest_universities'))
		facilities_data=eval(validated_data.pop('facilities'))
		amenities=list(map(lambda x:str(x)+"-amenities",facilities_data[0]['amenities']))
		safety_security=list(map(lambda x:str(x)+"-safetyAndSecurity",facilities_data[0]['safetyAndSecurity']))
		rent_inclusions=list(map(lambda x:str(x)+"-rentInclusions",facilities_data[0]['rentInclusions']))
		property_object=Property.objects.filter(id=instance.id).update(**validated_data)
		PropertyFacility.objects.filter(property_detail=instance.id).delete()
		PropertyUniversity.objects.filter(property_detail=instance.id).delete()
		amenities.extend(safety_security)
		amenities.extend(rent_inclusions)
		property_offers=[{'property_detail':property_object.id, **item} for item in json.loads(self.context.get('view').request.data['property_offers'])]
		property_offer_serializer=PropertyOfferSerializers(data=property_offers,many=True)
		if property_offer_serializer.is_valid():
			property_offer_serializer.save()

		for facility_detail in create_property_facilty(amenities):
			obj,created =PropertyFacility.objects.get_or_create(property_detail=instance,facilities=Facility.objects.get(id=facility_detail[0]),facilities_category=facility_detail[1],added_by=validated_data['added_by'])
		for university_id in university:
			obj,created	=	PropertyUniversity.objects.get_or_create(property_detail=instance,university=University.objects.get(id=university_id),added_by=validated_data['added_by']) 
		return instance

class PropertyWebsiteSerializer(PropertySerializer):
	# country_name=serializers.CharField(max_length=400,read_only=True)
	# city_name=serializers.CharField(max_length=400,read_only=True)
	# provider_name=serializers.CharField(max_length=400,read_only=True)
	# # facilities=serializers.CharField(max_length=2000,write_only=True)
	# # closest_universities=serializers.CharField(max_length=2000,write_only=True)
	# currency_symbol=serializers.CharField(max_length=400,read_only=True)
	# facilities_data=serializers.SerializerMethodField()
	# closest_universities
	near_by_university=serializers.SerializerMethodField()
	# property_offers=PropertyOfferSerializers(source='property_offer',many=True)
	# roomcategory=serializers.SerializerMethodField()
	# country_slug=serializers.SerializerMethodField()
	# city_slug=serializers.SerializerMethodField()
	# property_slug=serializers.SerializerMethodField()


	# country_name=serializers.CharField(max_length=250,read_only=True)
	# added_by_name=serializers.CharField(max_length=250,read_only=True)
	class Meta:
	
		fields = '__all__'
		#exclude = ('status', )
		model = Property

	# def get_university_slug(self,obj):
	# 	return generate_slug(obj.name)
	def get_near_by_university(self,obj):
		try:
			return [{"university_name":x.university.name,"city_name":x.university.city.name,"country_name":x.university.country.name,"description":x.university.description,"banner_image":x.university.banner_image,"logo":x.university.logo,"thumbnail":x.university.thumbnail,"has_campus":x.university.has_campus,"campus_detail":x.university.campus_detail,"latitude":x.university.latitude,"longitude":x.university.longitude,"university_id":x.university.id} for x in obj.property_university.all()]
		except Exception as e:
			# print(e)
			return None

	# def get_property_slug(self,obj):
	# 	try:
	# 		return generate_slug(obj.name)
	# 	except:
	# 		return None

class PropertySearchSerializer(PropertySerializer):
	category_name=serializers.CharField(default='Property')
	# country_name=serializers.CharField(max_length=400,read_only=True)
	# city_name=serializers.CharField(max_length=400,read_only=True)
	# provider_name=serializers.CharField(max_length=400,read_only=True)
	# # facilities=serializers.CharField(max_length=2000,write_only=True)
	# # closest_universities=serializers.CharField(max_length=2000,write_only=True)
	# currency_symbol=serializers.CharField(max_length=400,read_only=True)
	# facilities_data=serializers.SerializerMethodField()
	# closest_universities
	# near_by_university=serializers.SerializerMethodField()
	# property_offers=PropertyOfferSerializers(source='property_offer',many=True)
	# roomcategory=serializers.SerializerMethodField()
	# country_slug=serializers.SerializerMethodField()
	# city_slug=serializers.SerializerMethodField()
	# property_slug=serializers.SerializerMethodField()


	# country_name=serializers.CharField(max_length=250,read_only=True)
	# added_by_name=serializers.CharField(max_length=250,read_only=True)
	class Meta:
	
		fields = ('name','country_slug','city_slug','category_name')
		#exclude = ('status', )
		model = Property

	# def get_university_slug(self,obj):
	# 	return generate_slug(obj.name)
	# def get_near_by_university(self,obj):
	# 	try:
	# 		return [{"university_name":x.university.name,"city_name":x.university.city.name,"country_name":x.university.country.name,"description":x.university.description,"banner_image":x.university.banner_image,"logo":x.university.logo,"thumbnail":x.university.thumbnail,"has_campus":x.university.has_campus,"campus_detail":x.university.campus_detail,"latitude":x.university.latitude,"longitude":x.university.longitude,"university_id":x.university.id} for x in obj.property_university.all()]
	# 	except Exception as e:
	# 		# print(e)
	# 		return None