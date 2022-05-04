from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import(

    LoginView,
    ContactListView,
    AddContactView,
    EditContactView,
    ViewContactView,
    DeleteContactView,
    SearchContactView,
    

)
from . import views

urlpatterns = [

    path('',LoginView.as_view(),name='login'),
    path('contacts/',ContactListView.as_view(),name='contacts'),
    path('add_contact/',AddContactView.as_view(),name='add-contacts'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('edit_contact/<int:pk>/',EditContactView.as_view(),name='edit-contact'),
    path('view_contact/<int:pk>/',ViewContactView.as_view(),name='view-contact'),
    path('delete_contact/<int:pk>/',DeleteContactView.as_view(),name='delete-contact'),
    path('searched_contacts/',SearchContactView.as_view(),name='searched-contact')
    

    
]
