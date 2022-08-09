from django.urls import path
from .  import views


urlpatterns = [

 path('',views.allapiurls,name='allapiurls') ,
 path('all_contacts',views.get_all,name='all-contacts'),
 path('contact_detail/<int:id>/',views.get_contact,name="contact-detail"), 
 path('contact_create/',views.contact_create),
 path('contact_update/<int:id>',views.contact_update) ,
 path('contact_delete/<int:id>',views.delete_contact)
 

    
]
