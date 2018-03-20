from django.conf.urls import url
from . import views           
  
urlpatterns = [
    url(r'^', views.index),   
    url(r'^users/new$', views.new_user,  name='index'),     
    url(r'^/users/(?P<id>\d+)$', views.show, name='show'), #verify <id> format
    url(r'^/users/edit/(?P<id>\d+)$', views.editpage, name='editpage'),
    url(r'^/update/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^/users/destroy/(?P<id>\d+)$', views.destroy, name='destroy'),
    url(r'^register$', views.create, name='create'),
]
