from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('TalkDoc.views',

    url(r'^home/$', views.home, name='home'),

    #Profile
    url(r'^editProfile/$', views.edit_profile, name='edit_profile'),
    url(r'^user/profile/$', views.user_profile, name='user_profile'),
    url(r'^profile/view/(?P<id>[-\w]+)/(?P<appt_by>[-\w]+)/(?P<appt_id>[-\w]+)/$', views.view_profile, name='view_profile'),
    url(r'^profile/next/(?P<profile_id>[-\w]+)/(?P<step>[-\w]+)/$', views.show_next_step, name='show_next_step'),

    #Search
    url(r'^search/$', views.main_search, name='main_search'),
    url(r'^search/(?P<u_type>[-\w]+)/$', views.main_search, name='main_search'),
    url(r'^search/patient/$', views.patient_search, name='patient_search'),
    url(r'^search/patient/(?P<u_type>[-\w]+)/$', views.patient_search, name='patient_search'),

    # url(r'^searchResults/(?P<u_type>[-\w]+)/$', views.search_results, name='search_results'),

    #Appointments
    url(r'^reviews/$', views.appointments_reviews, name='appointments_reviews'),
    url(r'^approve/(?P<appt_id>[-\w]+)/(?P<service_id>[-\w]+)/$', views.approve_appointment, name='approve_appointment'),
    url(r'^decline/(?P<appt_id>[-\w]+)/(?P<service_id>[-\w]+)/$', views.decline_appointment, name='decline_appointment'),

    #Settings
    url(r'^settings/$', views.availability_settings, name='availability_settings'),
    url(r'^settings/(?P<id>[-\w]+)/$', views.availability_settings, name='availability_settings'),
    url(r'^settings/delete/(?P<id>[-\w]+)/$', views.delete_settings, name='delete_settings'),
    url(r'^services/settings/$', views.services_settings, name='services_settings'),
    url(r'^services/settings/(?P<id>[-\w]+)/$', views.services_settings, name='services_settings'),

    #Booking
    url(r'^booking/$', views.book_now, name='book_now'),
    url(r'^booking/(?P<app_by>[-\w]+)/(?P<app_to>[-\w]+)/(?P<appt_id>[-\w]+)/$', views.book_now, name='book_now'),
    url(r'^slots/$', views.get_time_slots, name='get_time_slots'),

    #Awards & Recognitions
    url(r'^award/add/(?P<id>[-\w]+)/$', views.add_award_item, name='add_award_item'),
    url(r'^award/submit/(?P<id>[-\w]+)/$', views.submit_award_item, name='submit_award_item'),
    url(r'^award/delete/(?P<id>[-\w]+)/$', views.delete_award_item, name='delete_award_item'),

    #Membership
    url(r'^membership/add/(?P<profile_id>[-\w]+)/$', views.add_membership_item, name='add_membership_item'),
    url(r'^membership/submit/(?P<id>[-\w]+)/$', views.submit_membership_item, name='submit_membership_item'),
    url(r'^membership/delete/(?P<id>[-\w]+)/$', views.delete_membership_item, name='delete_membership_item'),

    #Education
    url(r'^education/add/(?P<profile_id>[-\w]+)/$', views.add_education_item, name='add_education_item'),
    url(r'^education/submit/(?P<id>[-\w]+)/$', views.submit_education_item, name='submit_education_item'),
    url(r'^education/delete/(?P<id>[-\w]+)/$', views.delete_education_item, name='delete_education_item'),

    #Employment History
    url(r'^employment/add/(?P<profile_id>[-\w]+)/$', views.add_employment_item, name='add_employment_item'),
    url(r'^employment/submit/(?P<id>[-\w]+)/$', views.submit_employment_item, name='submit_employment_item'),
    url(r'^employment/delete/(?P<id>[-\w]+)/$', views.delete_employment_item, name='delete_employment_item'),

    #Speciality & Services
    url(r'^speciality/service/$', views.get_services_by_speciality, name='get_services_by_speciality'),
    url(r'^service/add/(?P<profile_id>[-\w]+)/$', views.add_speciality_services, name='add_speciality_services'),

    #Practice Location
    url(r'^location/add/(?P<profile_id>[-\w]+)/$', views.add_location_item, name='add_location_item'),
    url(r'^location/submit/(?P<id>[-\w]+)/$', views.submit_location_item, name='submit_location_item'),
    url(r'^location/delete/(?P<id>[-\w]+)/$', views.delete_location_item, name='delete_location_item'),

   )
