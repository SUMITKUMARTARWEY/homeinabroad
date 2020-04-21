from django.db import models

# Create your models here.
from django.contrib.auth.models import User

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

    class Meta:
        db_table='country'

class City(models.Model):
    id                   = models.AutoField(primary_key=True)
    name                 = models.CharField(max_length=500)
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

    class Meta:
        db_table='city'

class Provider(models.Model):
    id                      = models.AutoField(primary_key=True)
    name                    = models.CharField(max_length=500)
    # country                 = models.ForeignKey(Country,on_delete=models.CASCADE)
    enable_cancellation     = models.BooleanField()
    cancellation_description= models.TextField()
    # city                    = models.ForeignKey(City,on_delete=models.CASCADE)
    added_by                = models.ForeignKey(User,on_delete=models.CASCADE)
    added_date              = models.DateTimeField(auto_now_add=True)
    updated_date            = models.DateTimeField(auto_now=True)
    is_enabled              = models.IntegerField(default=1)

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
    added_by             = models.ForeignKey(User,on_delete=models.CASCADE)
    added_date           = models.DateTimeField(auto_now_add=True)
    updated_date         = models.DateTimeField(auto_now=True)
    is_enabled           = models.IntegerField(default=1)
    
    class Meta:
        db_table='facility'


class University(models.Model):
    id                   = models.AutoField(primary_key=True)
    name                 = models.CharField(max_length=500)
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
    # Name
    # campus Slug
    # isMainCampus
    # latitude
    # longitude
    
    class Meta:
        db_table='university'

# class Offer(models.Model):
#     id                   = models.AutoField(primary_key=True)
#     title                = models.CharField(max_length=500)
#     message              = models.TextField()
#     validity_date        = models.DateTimeField()
#     added_by             = models.ForeignKey(User,on_delete=models.CASCADE)
#     added_date           = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         db_table='offer'

# class RoomType(models.Model):
#     title            =  models.CharField(max_length=500)
#     type_area        =  models.TextField()
#     type_description =  models.TextField()
#     offers           =  models.TextField()
#     images           =  models.TextField()
#     bed_pricing      =  models.TextField()      
#     added_date       =  models.DateTimeField(auto_now_add=True)
#     updated_date     =  models.DateTimeField(auto_now=True)
#     is_enabled       =  models.IntegerField(default=1)

#     class Meta:
#         db_table='room_type'






# class RoomCategory(models.Model):
#     category_name           =   models.CharField(max_length=400)
#     category_description    =   models.TextField()
#     category_banner_imageurl=   models.TextField()
#     category_offer          =   models.TextField()
#     added_by                =   models.ForeignKey(User,on_delete=models.CASCADE)
#     updated_date            =   models.DateTimeField(auto_now=True)
#     added_date              =   models.DateTimeField(auto_now_add=True)
#     room_type               =   models.ForeignKey(RoomType,on_delete=models.ForeignKey)
#     #added_date              =   models.DateTimeField(auto_now_add=True)
#     #updated_date            =   models.DateTimeField(auto_now=True)
#     is_enabled              =   models.IntegerField(default=1)
#     class Meta:
#         db_table='room_categories'



class Property(models.Model):
    id                          = models.AutoField(primary_key=True)
    name                        = models.CharField(max_length=400)
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
    property_offers             = models.TextField()
    property_images             = models.TextField()  
    heading1                    = models.TextField()
    heading2                    = models.TextField()
    meta_title                  = models.TextField() 
    meta_keywords               = models.TextField()
    meta_description            = models.TextField()
    room_categories             = models.TextField()
    added_by                    = models.ForeignKey(User,on_delete=models.CASCADE)
    added_date                  = models.DateTimeField(auto_now_add=True)
    updated_date                = models.DateTimeField(auto_now=True)


    class Meta:
        db_table='property'

class PropertyUniversity(models.Model):
    id                      = models.AutoField(primary_key=True)
    property_detail         = models.ForeignKey(Property,on_delete=models.CASCADE)
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

    # "propertyImages": [], 
    # "facilities": [
    #     {
    #         "propertyAmenities": [
    #             {
    #                 "iconUrl": 
    #                 "",
    #                 "iconName": ""
    #             }
    #         ]
    #     },
    #     {
    #         "propertyRentInclusions": [
    #             {
    #                 "iconUrl": "",
    #                 "iconName": ""
    #             }
    #         ]
    #     },
    #     {
    #         "propertySafetySecurityInclusions": [
    #             {
    #                 "iconUrl": "",
    #                 "iconName": ""
    #             }
    #         ]
    #     }
    # ],
    # "universitiesNearby": [
    #     {
    #         "name": "",
    #         "city": "",
    #         "country": "",

    #         "slug": "",
    #         "campuses": [
    #             {
    #                 "lat": 0,
    #                 "lng": 0,
    #                 "slug": "",
    #                 "name": ""
    #             }
    #         ]
    #     }
    # ],
    # "roomCategories": [
    #     {
    #         "categoryName": "",
    #         "categoryDescription": "",
    #         "categoryBannerImageUrl": [],
    #         "categoryOffer": {
    #             "offerTitle": "",
    #             "offerDescription": "",
    #             "offerValidityDate": ""
    #         },
    #         "roomTypes": [
    #             {
    #                 "typeTitle": "",
    #                 "typeArea": "",
    #                 "typeDescription": "",
    #                 "typeOffer": [
    #                     {
    #                         "offerTitle": "",
    #                         "offerDescription": "",
    #                         "offerValidityDate": ""
    #                     }
    #                 ],
    #                 "typeImages": [],
    #                 "bedPricing": [
    #                     {
    #                         "isShortTerm" : false,
    #                         "hasNominatedBeds" : false,
    #                         "numberOfNominatedBeds" : 0,
    #                         "bedAvailabilityStatus" : "",
    #                         "rentBreakupDuration" : "",
    #                         "tenancyDuration" : 0,
    #                         "tenancyDurationUnit" : "",
    #                         "roomCheckInDate" : "",
    #                         "roomCheckOutDate" : "",
    #                         "bedPrice" : 0,
    #                         "bedDiscountedPrice" : 0,
    #                         "depositCharge" : 0,
    #                         "serviceFee" : 0,
    #                         "taxesInclusive" : 0
    #                     }
    #                 ]
    #             }
    #         ]
    #     }
    # ],
    # "meta": {
      #  "metaH1": "",
      # "metaH2": "",
       # "metaTitle": "",
        #"metaKeywords": "",
        #"metaDescription": ""
    # }


































    
    
    
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