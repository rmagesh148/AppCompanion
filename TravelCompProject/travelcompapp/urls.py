from django.conf.urls import url 
from travelcompapp import views 

urlpatterns = [
    url(r'^getuserlist$', views.user_list),
    url(r'^getuser$', views.user)
]