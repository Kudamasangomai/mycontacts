from django import views
from django.urls import path
from . import views


urlpatterns = [

    path('',views.ajax_contact_list,name="ajax-contact-list")
  
]


