from django.conf.urls import url 
from travelcompapp import views 

urlpatterns = [
    url(r'^$', views.home),
    url(r'^getuserlist$', views.user_list),
    url(r'^getuser$', views.user),
    url(r'^travelinfo$', views.travel_info_create_get),
    url(r'^travelinfogroupby$', views.get_info_group_flight_no),
    url(r'^getairportcity$', views.get_airport_city)
]