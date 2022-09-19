from django.urls import re_path 
from travelcompapp import views 

urlpatterns = [
    re_path(r'^$', views.home),
    re_path(r'^getuserlist$', views.user_list),
    re_path(r'^getuser$', views.user),
    re_path(r'^travelinfo$', views.travel_info_create_get),
    re_path(r'^travelinfogroupby$', views.get_info_group_flight_no),
    re_path(r'^getairportcity$', views.get_airport_city)
]