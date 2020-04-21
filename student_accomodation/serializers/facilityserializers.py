from student_accomodation.models import Facility
from student_accomodation.views import university
from rest_framework import serializers
from .stundent_manager import generate_slug
class FacilitySerializer(serializers.ModelSerializer):
	facility_slug=serializers.SerializerMethodField()
	# country_name=serializers.CharField(max_length=250,read_only=True)
	added_by_name=serializers.CharField(max_length=250,read_only=True)
	class Meta:
		# fields = ('id','scale','banker_name','branch_detail','email','current_mobile','old_mobile_no1','old_mobile_no2','notes','marketer','level2_profile','level3_profile','is_deleted','bank','bank_name','bank','marketer_name','status','visiting_card','added_date','banker_mobile','firm','firm_name',)
		fields = '__all__'
		#exclude = ('status', )
		model = Facility
	def get_facility_slug(self,obj):
		return generate_slug(obj.title)