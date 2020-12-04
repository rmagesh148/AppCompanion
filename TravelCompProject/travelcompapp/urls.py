from django.conf.urls import url 
from travelcompapp import views 

urlpatterns = [
    url(r'^$', views.home),
    url(r'^getuserlist$', views.user_list, name = 'user_list'),
    url(r'^getuser$', views.user,name = 'user')
]