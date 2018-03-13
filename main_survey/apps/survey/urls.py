from django.conf.urls import url
from . import views           
  
urlpatterns = [
    url(r'^$', views.index),   
    url(r'survey/create', views.create),     
    url(r'survey/result', views.result)  ,
    url(r'survey/return', views.returned)  ,

]