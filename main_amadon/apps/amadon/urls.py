from django.conf.urls import url
from . import views           
  
urlpatterns = [
    url(r'^$', views.index),   
    url(r'amadon/create', views.create),     
    url(r'amadon/result', views.result)  ,
    url(r'amadon/returned', views.returned)  ,

]