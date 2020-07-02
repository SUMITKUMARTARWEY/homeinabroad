from django.db import models

# Create your models here.
from django.contrib.auth.models import User 
from django.utils.text import slugify 

class Currency(models.Model):
    id                   = models.AutoField(primary_key=True)
    currency_code        = models.CharField(max_length=500)
    added_by             = models.ForeignKey(User,on_delete=models.CASCADE)
    added_date           = models.DateTimeField(auto_now_add=True)
    updated_date         = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='currency_code'


class Country(models.Model):
    id                   = models.AutoField(primary_key=True)
    name                 = models.CharField(max_length=500)
    country_slug         = models.SlugField(max_length=500,null=True,blank=True,editable=False)          
    country_code         = models.CharField(max_length=500)
    currency_code        = models.ForeignKey(Currency,on_delete=models.CASCADE,null=True,blank=True)
    currency_symbol      = models.TextField(max_length=500)
    banner_image         = models.TextField() 
    country_logo         = models.TextField(max_length=500)
    country_thumbnail    = models.TextField()
    description          = models.TextField()         
    country_ranking      = models.PositiveIntegerField()
    isfeatured           = models.BooleanField()
    heading1             = models.TextField()
    heading2             = models.TextField()
    meta_title           = models.CharField(max_length=500)
    meta_keyword         = models.TextField()
    meta_description     = models.TextField()
    added_date           = models.DateTimeField(auto_now_add=True)
    updated_date         = models.DateTimeField(auto_now=True)
    is_enabled           = models.IntegerField(default=1)
    added_by             = models.ForeignKey(User,on_delete=models.CASCADE)

    def save(self, *args, **kwargs): 
        if  self.id is None:
            self.country_slug = slugify(self.name)
            country=Country.objects.filter(country_slug=self.country_slug).exists()
            if country is True:
                country_lated_id=Country.objects.latest('id')
                # print(city_lated_id.id)
                self.country_slug=slugify("{} {}".format(self.name,country_lated_id.id+1))
        super(Country, self).save(*args, **kwargs) 

    class Meta:
        db_table='country'

class City(models.Model):
    id                   = models.AutoField(primary_key=True)
    name                 = models.CharField(max_length=500)
    city_slug            = models.SlugField(max_length=500,null=True,blank=True,editable=False)
    country              = models.ForeignKey(Country,on_delete=models.CASCADE)
    city_description     = models.TextField()
    city_banner_image    = models.TextField()
    city_logo            = models.TextField()
    city_thumbnail       = models.TextField()
    description          = models.TextField()
    is_featured          = models.BooleanField()
    city_ranking         = models.PositiveIntegerField()
    latitude             = models.FloatField()
    longitude            = models.FloatField()
    heading1             = models.TextField()
    heading2             = models.TextField()
    meta_title           = models.CharField(max_length=500)
    meta_keyword         = models.TextField()
    meta_description     = models.TextField()
    added_date           = models.DateTimeField(auto_now_add=True)
    updated_date         = models.DateTimeField(auto_now=True)
    status               = models.IntegerField(default=1)
    added_by             = models.ForeignKey(User,on_delete=models.CASCADE)
    is_enabled           = models.IntegerField(default=1)

    def save(self, *args, **kwargs): 
        if  self.id is None:
            self.city_slug = slugify(self.name)
            city=City.objects.filter(city_slug=self.city_slug).exists()
            if city is True:
                city_lated_id=City.objects.latest('id')
                # print(city_lated_id.id)
                self.city_slug=slugify("{} {}".format(self.name,city_lated_id.id+1))   
        super(City, self).save(*args, **kwargs) 

    class Meta:
        db_table='city'

class Provider(models.Model):
    id                      = models.AutoField(primary_key=True)
    name                    = models.CharField(max_length=500)
    provider_slug           = models.SlugField(max_length=300,null=True,blank=True,editable=False)
    # country                 = models.ForeignKey(Country,on_delete=models.CASCADE)
    enable_cancellation     = models.BooleanField()
    cancellation_description= models.TextField()
    # city                    = models.ForeignKey(City,on_delete=models.CASCADE)
    added_by                = models.ForeignKey(User,on_delete=models.CASCADE)
    added_date              = models.DateTimeField(auto_now_add=True)
    updated_date            = models.DateTimeField(auto_now=True)
    is_enabled              = models.IntegerField(default=1)

    def save(self, *args, **kwargs): 
        if  self.id is None:
            self.provider_slug = slugify(self.name)
            provider=Provider.objects.filter(provider_slug=self.provider_slug).exists()
            if provider is True:
                provider_lated_id=Provider.objects.latest('id')
                self.provider_slug=slugify("{} {}".format(self.name,provider_lated_id.id+1))
        super(Provider, self).save(*args, **kwargs) 
    class Meta:
        db_table='provider'

class ProviderCity(models.Model):
    id                      = models.AutoField(primary_key=True)
    provider                = models.ForeignKey(Provider,on_delete=models.CASCADE,related_name='provider_city')
    city                    = models.ForeignKey(City,on_delete=models.CASCADE)
    added_by                = models.ForeignKey(User,on_delete=models.CASCADE)
    added_date              = models.DateTimeField(auto_now_add=True)
    updated_date            = models.DateTimeField(auto_now=True)
    is_enabled              = models.IntegerField(default=1)

    class Meta:
        db_table='provider_city'


class Facility(models.Model):
    id                   = models.AutoField(primary_key=True)
    logo                 = models.CharField(max_length=500)
    title                = models.TextField()
    facility_slug        = models.SlugField(max_length=400,null=True,blank=True,editable=False)
    added_by             = models.ForeignKey(User,on_delete=models.CASCADE)
    added_date           = models.DateTimeField(auto_now_add=True)
    updated_date         = models.DateTimeField(auto_now=True)
    is_enabled           = models.IntegerField(default=1)

    def save(self, *args, **kwargs): 
        if  self.id is None:
            self.facility_slug = slugify(self.title)
            facility=Facility.objects.filter(facility_slug=self.facility_slug).exists()
            if facility is True:
                facility_lated_id=Facility.objects.latest('id')
                self.facility_slug=slugify("{} {}".format(self.title,facility_lated_id.id+1))
        super(Facility, self).save(*args, **kwargs)
    
    class Meta:
        db_table='facility'


class University(models.Model):
    id                   = models.AutoField(primary_key=True)
    name                 = models.CharField(max_length=500)
    university_slug      = models.SlugField(max_length=500,null=True,blank=True,editable=False)
    city                 = models.ForeignKey(City,on_delete=models.CASCADE)
    country              = models.ForeignKey(Country,on_delete=models.CASCADE)
    description          = models.TextField()
    banner_image         = models.TextField()
    logo                 = models.TextField()
    thumbnail            = models.TextField()
    has_campus           = models.BooleanField(max_length=500)
    campus_detail        = models.TextField()
    added_by             = models.ForeignKey(User,on_delete=models.CASCADE)
    added_date           = models.DateTimeField(auto_now_add=True)
    updated_date         = models.DateTimeField(auto_now=True)
    is_enabled           = models.IntegerField(default=1)
    latitude             = models.FloatField()
    longitude            = models.FloatField()
    heading1             = models.TextField()
    heading2             = models.TextField()
    meta_title           = models.CharField(max_length=500)
    meta_keyword         = models.TextField()
    meta_description     = models.TextField()

    def save(self, *args, **kwargs): 
        if  self.id is None:
            self.university_slug = slugify(self.name)
            university=University.objects.filter(university_slug=self.university_slug).exists()
            if university is True:
                university_lated_id=University.objects.latest('id')
                self.university_slug=slugify("{} {}".format(self.name,university_lated_id.id+1)) 
        super(University, self).save(*args, **kwargs) 
    
    
    class Meta:
        db_table='university'
 
class Property(models.Model):
    id                          = models.AutoField(primary_key=True)
    name                        = models.CharField(max_length=400)
    slug                        = models.SlugField(max_length=200,null=True,blank=True,editable=False)
    description                 = models.TextField()
    distance_from_city_center   = models.FloatField(default=0)
    provider                    = models.ForeignKey(Provider,on_delete=models.CASCADE)
    latitude                    = models.FloatField()
    longitude                   = models.FloatField()
    address                     = models.TextField()
    isfeatured                  = models.BooleanField()
    country                     = models.ForeignKey(Country,on_delete=models.CASCADE)
    city                        = models.ForeignKey(City,on_delete=models.CASCADE)
    numbers_of_beds             = models.IntegerField()
    ranking                     = models.IntegerField()
    property_type               = models.CharField(max_length=500)
    rating                      = models.FloatField()
    base_currency_code          = models.CharField(max_length=500)
   # offers                  = models.ForeignKey(Offer,on_delete=models.Model)
    whybook                     = models.TextField()
    payment_procedure           = models.TextField()
    is_enabled                  = models.IntegerField(default=1)
    ispropertyextraOrdinary     = models.IntegerField(default=1)
    #is_soldOut                  = models.IntegerField(default=1)
    # propertyranking         = models.IntegerField(default=0)
    #propertyaddress             = models.TextField()
    propertylistingorder        = models.IntegerField()
    # numberofbeds            = models.TextField()
    #property_speciality         = models.TextField()
    #property_payment_rules      = models.TextField()
    # offers                      = models.ForeignKey(Offer,on_delete=models.CASCADE)
    property_images             = models.TextField()  
    heading1                    = models.TextField()
    heading2                    = models.TextField()
    meta_title                  = models.TextField() 
    meta_keywords               = models.TextField()
    meta_description            = models.TextField()
    # room_categories             = models.TextField()
    added_by                    = models.ForeignKey(User,on_delete=models.CASCADE)
    added_date                  = models.DateTimeField(auto_now_add=True)
    updated_date                = models.DateTimeField(auto_now=True)             
    
    def save(self, *args, **kwargs): 
        if  self.id is None:
            self.slug = slugify(self.name)
            property_detail=Property.objects.filter(slug=self.slug).exists()
            if property_detail is True:
                property_lated_id=Property.objects.latest('id')
                self.slug=slugify("{} {}".format(self.name,property_lated_id.id+1)) 
        super(Property, self).save(*args, **kwargs)  

    class Meta:
        db_table='property'



     # print("njkkjjnnj")
class PropertyOffers(models.Model):
    id                          = models.AutoField(primary_key=True)
    property_detail             = models.ForeignKey(Property,on_delete=models.CASCADE,related_name='property_offer')
    title                       = models.CharField(max_length=500)
    message                     = models.TextField()
    validity_date               = models.DateField()
    # added_by                    =   models.ForeignKey(User,on_delete=models.CASCADE)
    # updated_date                =   models.DateTimeField(auto_now=True)
    # added_date                  =   models.DateTimeField(auto_now_add=True)
    # room_type               =   models.ForeignKey(RoomType,on_delete=models.ForeignKey)
    #added_date              =   models.DateTimeField(auto_now_add=True)
    #updated_date            =   models.DateTimeField(auto_now=True)
    is_enabled                  =   models.IntegerField(default=1)

    class Meta:
        db_table='property_offer'

# def remove_books(sender, instance, **kwargs):
#     author_id = instance.id
#     print(kwargs)
#     # PropertyOffers.objects.filter(author_id=author_id).delete()
# signals.post_save.connect(remove_books, sender=Property)


class RoomCategory(models.Model):
    id                      =   models.AutoField(primary_key=True)
    property_detail         =   models.ForeignKey(Property,on_delete=models.CASCADE,related_name='property_category')
    category_name           =   models.CharField(max_length=400)
    category_description    =   models.TextField()
    category_banner_imageurl=   models.TextField()
    # category_offer          =   models.TextField()
    # added_by                =   models.ForeignKey(User,on_delete=models.CASCADE)
    updated_date            =   models.DateTimeField(auto_now=True)
    added_date              =   models.DateTimeField(auto_now_add=True)
    # room_type               =   models.ForeignKey(RoomType,on_delete=models.ForeignKey)
    #added_date              =   models.DateTimeField(auto_now_add=True)
    #updated_date            =   models.DateTimeField(auto_now=True)
    is_enabled              =   models.IntegerField(default=1)
    class Meta:
        db_table='room_categories'

class RoomCategoryOffer(models.Model):
    id                      = models.AutoField(primary_key=True)
    roomcategory            = models.ForeignKey(RoomCategory,on_delete=models.CASCADE,related_name='roomcategory')
    # Offer                   = models.ForeignKey(Offer,on_delete=models.CASCADE)
    title                   = models.CharField(max_length=500)
    message                 = models.TextField()
    validity_date           = models.DateField()
    # added_by                = models.ForeignKey(User,on_delete=models.CASCADE)
    added_date              = models.DateTimeField(auto_now_add=True)
    is_enabled              = models.IntegerField(default=1)

    class Meta:
        db_table='room_categories_offer'



class RoomType(models.Model):
    id               = models.AutoField(primary_key=True)
    title            = models.CharField(max_length=500)
    type_area        = models.TextField()
    roomcategory     = models.ForeignKey(RoomCategory,on_delete=models.CASCADE,related_name='room_type_category')
    type_description = models.TextField()
    images           = models.TextField()
    added_date       = models.DateTimeField(auto_now_add=True)
    is_enabled       = models.IntegerField(default=1)

    class Meta:
        db_table='room_type'




class RoomTypeOffer(models.Model):
    id                  = models.AutoField(primary_key=True)
    roomtype            = models.ForeignKey(RoomType,on_delete=models.CASCADE,related_name='room_type_offer')
    # Offer               = models.ForeignKey(Offer,on_delete=models.CASCADE)
    title               = models.CharField(max_length=500)
    message             = models.TextField()
    validity_date       = models.DateField()
    # added_by            = models.ForeignKey(User,on_delete=models.CASCADE)
    added_date          = models.DateTimeField(auto_now_add=True)
    is_enabled          = models.IntegerField(default=1)

    class Meta:
        db_table='roomtype_offer'


class BedPricing(models.Model):
    id                    = models.AutoField(primary_key=True)
    roomtype              = models.ForeignKey(RoomType,on_delete=models.CASCADE,related_name='roomtype_bed_pricing')
    is_shortterm          = models.BooleanField(default=True)
    hasnominatedbeds      = models.BooleanField(default=True)
    numberofnominatedbeds = models.IntegerField(default=0)
    bedavailabilitystatus = models.TextField()
    rentbreakup_duration  = models.CharField(max_length=400)
    tenancy_duration      = models.CharField(max_length=400)
    tenancy_durationunit  = models.CharField(max_length=400)
    room_checkin_date     = models.DateField()
    room_checkout_date    = models.DateField()
    bed_price             = models.IntegerField(default=0)
    bed_discounted_price  = models.IntegerField()
    deposit_charge        = models.IntegerField(default=0)
    service_fee           = models.IntegerField(default=0)
    taxes_inclusive       = models.IntegerField(default=0)
    display_price_bed     = models.TextField()
    display_discount_price_bed=models.TextField()

    class Meta:
        db_table='bed_price'


class PropertyUniversity(models.Model):
    id                      = models.AutoField(primary_key=True)
    property_detail         = models.ForeignKey(Property,on_delete=models.CASCADE,related_name='property_university')
    university              = models.ForeignKey(University,on_delete=models.CASCADE)
    added_date              = models.DateTimeField(auto_now_add=True)
    updated_date            = models.DateTimeField(auto_now=True)
    added_by                = models.ForeignKey(User,on_delete=models.CASCADE)
    is_enabled              = models.IntegerField(default=1)

    class Meta:
        db_table='property_university'

class PropertyFacility(models.Model):
    id                      = models.AutoField(primary_key=True)
    property_detail         = models.ForeignKey(Property,on_delete=models.CASCADE,related_name='property_facility')
    facilities              = models.ForeignKey(Facility,on_delete=models.CASCADE)
    facilities_category     = models.TextField()
    added_date              = models.DateTimeField(auto_now_add=True)
    updated_date            = models.DateTimeField(auto_now=True)
    added_by                = models.ForeignKey(User,on_delete=models.CASCADE)
    is_enabled              = models.IntegerField(default=1)

    class Meta:
        db_table='property_facility'

class ContactUs(models.Model):
    id                     = models.AutoField(primary_key=True)
    name                   = models.CharField(max_length=500)
    email                  = models.EmailField()
    contact_no             = models.CharField(max_length=500)
    message                = models.TextField()
    lead_source            = models.TextField()
    # added_by               = models.ForeignKey(User,on_delete=models.CASCADE)
    added_date             = models.DateTimeField(auto_now_add=True)
    is_enabled             = models.IntegerField(default=1)                 

    class Meta:
        db_table='contact_us'


class RequestService(models.Model):
    id                     = models.AutoField(primary_key=True)
    first_name             = models.CharField(max_length=500)
    last_name              = models.CharField(max_length=500)
    email                  = models.EmailField()
    contact_number         = models.CharField(max_length=500) 
    message                = models.TextField()
    service_name           = models.TextField()
    is_enabled             = models.IntegerField(default=1)
    # added_by               = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        db_table='request_service'

class Booking(models.Model):
    id                     = models.AutoField(primary_key=True)
    first_name             = models.CharField(max_length=500) 
    last_name              = models.CharField(max_length=500)
    gender                 = models.CharField(max_length=200)
    email                  = models.EmailField()
    contact_number         = models.CharField(max_length=200)
    dob                    = models.DateField()
    nationality            = models.CharField(max_length=200)
    city                   = models.ForeignKey(City,on_delete=models.CASCADE)
    postal_code            = models.CharField(max_length=200)
    university             = models.ForeignKey(University,on_delete=models.CASCADE)
    year_of_study          = models.IntegerField()
    lead_source            = models.TextField()
    property_name          = models.TextField()
    property_detail        = models.ForeignKey(Property,on_delete=models.CASCADE)
    room_type              = models.ForeignKey(RoomType,on_delete=models.CASCADE)
    bed_price              = models.ForeignKey(BedPricing,on_delete=models.CASCADE)
    check_in_date          = models.DateField()
    checkout_date          = models.DateField()
    added_date             = models.DateTimeField()
    is_enabled             = models.IntegerField(default=1)

    class Meta:
        db_table='booking'

class Enquiry(models.Model):
    id                     = models.AutoField(primary_key=True)
    first_name             = models.CharField(max_length=500)
    last_name              = models.CharField(max_length=500)
    email                  = models.EmailField()
    contact_number         = models.CharField(max_length=200)
    university             = models.ForeignKey(University,on_delete=models.CASCADE)
    lead_source            = models.TextField()
    message                = models.TextField()
    property_detail        = models.ForeignKey(Property,on_delete=models.CASCADE)
    room_category          = models.ForeignKey(RoomCategory,on_delete=models.CASCADE)
    room_type              = models.ForeignKey(RoomType,on_delete=models.CASCADE)  
    bed_price              = models.ForeignKey(BedPricing,on_delete=models.CASCADE)
    check_in_date          = models.DateField()
    checkout_date          = models.DateField()
    is_enabled             = models.IntegerField(default=1)

    class Meta:
        db_table='enquiry'

class LeadGeneration(models.Model):    
    first_name              = models.CharField(max_length=400)
    last_name               = models.CharField(max_length=400)
    email                   = models.EmailField()
    contact_number          = models.CharField(max_length=400)
    university              = models.ForeignKey(University,on_delete=models.CASCADE)
    lead_source             = models.CharField(max_length=400)
    message                 = models.TextField()
    budget                  = models.TextField(null=True,blank=True)
    room_type               = models.ForeignKey(RoomType,on_delete=models.CASCADE)

    class Meta:
        db_table='lead_generation'
   

































    
    
    
#     # nearby_universities (Fields from Universities Table)
#     # room_categories

#     class Meta:
#         db_table='property' 


# class PropertyFeatures(models.Model):
#     id              = models.AutoField(primary_key=True)
#     alt_tag         = models.TextField()
#     url             = models.TextField()
#     property_type   = models.TextField()

#     class Meta:
#         db_table='property_feature'

# class PropertyImage(models.Model):
#     url             = models.CharField(max_length=500)
#     alt_tag         = CharField(max_length=500)
#     ranking         = models.IntegerField()
#     image_level     = models.TextField()
#     class Meta:
#         db_table='property_image'