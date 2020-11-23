from django.conf.urls import url, include
from django.urls import path

from . import views



urlpatterns = [
     path ('<int:blog_id>/',views.details, name='details'),
    path('',views.allblogs,name='allblogs'),
   ]