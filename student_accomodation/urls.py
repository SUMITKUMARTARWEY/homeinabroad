from django.conf.urls import url,include
from .views import user,city,university,country,provider,facility,property_view,currency,contactus,requestservice,booking,enquiry,leadgenration

from django.conf.urls.static import static

urlpatterns =[
			url(r'^user/list/$',user.list.as_view(),name='user_list'),			
			url(r'^user/show/(?P<pk>[0-9]+)$',user.show.as_view(),name="user_show"),
			url(r'^country/list/',country.list.as_view(),name='country_list'),
			url(r'country/show/(?P<pk>[0-9]+)$',country.show.as_view(),name='country_show'),
			url(r'^city/list/$',city.list.as_view(),name='city_list'),			
			url(r'^city/show/(?P<pk>[0-9]+)$',city.show.as_view(),name="city_show"),
			url(r'^university/list/',university.list.as_view(),name='university_list'),
			url(r'^university/show/(?P<pk>[0-9]+)$',university.show.as_view(),name='university_show'),
			url(r'^provider/list/',provider.list.as_view(),name='provider_list'),
			url(r'^provider/show/(?P<pk>[0-9]+)$',provider.show.as_view(),name='provider_show'),
			url(r'^facility/list/',facility.list.as_view(),name='facility_list'),
			url(r'^facility/show/(?P<pk>[0-9]+)$',facility.show.as_view(),name='facility_show'),
			url(r'^property/list/$',property_view.list.as_view(),name='property_list'),
			url(r'^property/show/(?P<pk>[0-9]+)$',property_view.show.as_view(),name='property_show'),
			url(r'^countrycode/list/$',currency.list.as_view(),name='countrycode_list'),
			url(r'^countrycode/show/(?P<pk>[0-9]+)$',currency.show.as_view(),name='countrycode_show'),
			url(r'^leadgenration/list/$',leadgenration.list.as_view(),name='countrycode_list'),
			url(r'^leadgenration/show/(?P<pk>[0-9]+)$',leadgenration.show.as_view(),name='countrycode_show'),
			url(r'^enquiry/list/$',enquiry.list.as_view(),name='countrycode_list'),
			url(r'^enquiry/show/(?P<pk>[0-9]+)$',enquiry.show.as_view(),name='countrycode_show'),
			url(r'^booking/list/$',booking.list.as_view(),name='countrycode_list'),
			url(r'^booking/show/(?P<pk>[0-9]+)$',booking.show.as_view(),name='countrycode_show'),
			url(r'^requestservice/list/$',requestservice.list.as_view(),name='countrycode_list'),
			url(r'^requestservice/show/(?P<pk>[0-9]+)$',requestservice.show.as_view(),name='countrycode_show'),
			url(r'^contactus/list/$',contactus.list.as_view(),name='countrycode_list'),
			url(r'^contactus/show/(?P<pk>[0-9]+)$',contactus.show.as_view(),name='countrycode_show'),
			]

