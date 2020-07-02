from student_accomodation.models import University
# from student_accomodation.views import university
from rest_framework import serializers
from .stundent_manager import generate_slug
import json
class UniversitySerializer(serializers.ModelSerializer):
	# university_slug=serializers.SerializerMethodField()
	added_by_name=serializers.CharField(max_length=400,read_only=True)
	country_name=serializers.CharField(max_length=400,read_only=True)
	city_name=serializers.CharField(max_length=400,read_only=True)
	campus_detail_data=serializers.SerializerMethodField()
	# country_name=serializers.CharField(max_length=250,read_only=True)
	# added_by_name=serializers.CharField(max_length=250,read_only=True)
	class Meta:
		# fields = ('id','scale','banker_name','branch_detail','email','current_mobile','old_mobile_no1','old_mobile_no2','notes','marketer','level2_profile','level3_profile','is_deleted','bank','bank_name','bank','marketer_name','status','visiting_card','added_date','banker_mobile','firm','firm_name',)
		fields = '__all__'
		# exclude = ('status', )
		model = University

	# def get_university_slug(self,obj):
	# 	return generate_slug(obj.name)

	def get_campus_detail_data(self,obj):
		try:
			return json.loads(obj.campus_detail)
		except Exception as e:
			return None

class UniversityCitySerializer(UniversitySerializer):
	# university_slug=serializers.SerializerMethodField()
	# added_by_name=serializers.CharField(max_length=400,read_only=True)
	# country_name=serializers.CharField(max_length=400,read_only=True)
	# city_name=serializers.CharField(max_length=400,read_only=True)
	# campus_detail_data=serializers.SerializerMethodField()
	city_slug=serializers.SerializerMethodField()
	# country_name=serializers.CharField(max_length=250,read_only=True)
	# added_by_name=serializers.CharField(max_length=250,read_only=True)
	class Meta:
		# fields = ('id','scale','banker_name','branch_detail','email','current_mobile','old_mobile_no1','old_mobile_no2','notes','marketer','level2_profile','level3_profile','is_deleted','bank','bank_name','bank','marketer_name','status','visiting_card','added_date','banker_mobile','firm','firm_name',)
		fields = '__all__'
		#exclude = ('status', )
		model = University

	# def get_university_slug(self,obj):
	# 	return generate_slug(obj.name)

	# def get_campus_detail_data(self,obj):
	# 	try:
	# 		return json.loads(obj.campus_detail)
	# 	except Exception as e:
	# 		return None
	def get_city_slug(self,obj):
		try:
			return (obj.city.city_slug)
		except:
			return None

	class Meta:
		# fields = ('id','scale','banker_name','branch_detail','email','current_mobile','old_mobile_no1','old_mobile_no2','notes','marketer','level2_profile','level3_profile','is_deleted','bank','bank_name','bank','marketer_name','status','visiting_card','added_date','banker_mobile','firm','firm_name',)
		# fields = ('name','university_slug','')
		#exclude = ('status', )
		fields='__all__'
		model = University

class UniversitySearchSerializer(UniversityCitySerializer):
	country_slug=serializers.SerializerMethodField()

	class Meta:
		model  = University
		fields = ('name','university_slug','city_slug','country_slug')

	def get_country_slug(self,obj):
		try:
			return obj.country.country_slug
		except:
			return None