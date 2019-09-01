

from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
      path('', views.home , name='home_page'),
      path('academics', views.academics , name='academics'),
       path('new', views.academics , name='new'),
       path('test',views.test,name="test"),
      ]