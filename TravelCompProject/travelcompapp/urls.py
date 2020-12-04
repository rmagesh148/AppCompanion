from django.conf.urls import url 
from travelcompapp import views 

urlpatterns = [
<<<<<<< HEAD
    url(r'^$', views.home),
    url(r'^getuserlist$', views.user_list, name = 'user_list'),
    url(r'^getuser$', views.user,name = 'user')
=======
    url(r'^getuserlist$', views.user_list),
    url(r'^getuser$', views.user),
    url(r'^travelinfo$', views.travel_info_create_get),
    url(r'^travelinfogroupby$', views.get_info_group_flight_no)
>>>>>>> 833eadc4ebb79d9f14e47a759303eaf4dd6864de
]