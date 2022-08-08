from django.views.generic import ListView , CreateView ,UpdateView ,DetailView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render #works with function based View
from .forms import AddContactForm
from .models import contacts
from django.conf import settings
from django.db.models import Q


#login view 
class LoginView(LoginView):
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True



class ContactListView(LoginRequiredMixin,ListView):
    model = contacts # the model /database we are getting out data
    template_name = 'main/contacts.html'  # were we going to display i.e the html page
    context_object_name = 'contacts' #variable name we will use to loop through the data
    paginate_by = 6 #paginating 

    #this method overrides the default query to match want we want
    def get_queryset(self,**kwargs):
        queryset = super(ContactListView, self).get_queryset()
        queryset = contacts.objects.filter(userid = self.request.user )
        return queryset


class AddContactView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = contacts
    form_class = AddContactForm
    template_name = 'main/add-contacts.html'
    success_message = 'Contact successfully Added'
    #success_url = reverse_lazy('contacts')we can redirect here or use the absolute url in contacts model.py

    def form_valid(self,form):
        form.instance.userid = self.request.user #adding the logged in user to the form instance
        return super().form_valid(form)
    
    
class EditContactView(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,UpdateView):
    model = contacts
    form_class = AddContactForm
    #fields =['contact_lastname']
    template_name = 'main/add-contacts.html'
    #success_url = reverse_lazy('contacts')#taken care by the DB
    success_message = 'Contact successfully Updated'

    def form_valid(self,form):
        form.instance.userid = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        contact = self.get_object()
        if self.request.user == contact.userid:
            return True
        return    

class ViewContactView(LoginRequiredMixin,DetailView):
    model = contacts
    template_name = 'main/view-contact.html'

    def test_func(self):
        contact = self.get_object()
        if self.request.user == contact.userid:
            return True
        return False 

class DeleteContactView(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,DeleteView):
    model = contacts
    success_url = reverse_lazy('contacts')
    success_message = "Contact SuccessFully Deleted"

    #test and see if the user who wants to delete it is the owner
    def test_func(self):
        contact = self.get_object()
        if self.request.user == contact.userid:
            return True
        return False  

class SearchContactView(LoginRequiredMixin,ListView):
    model = contacts
    template_name = 'main/searchcontact.html'
    context_object_name = 'searchcontact'

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('searchcontact') #getting wht the user has entered
        object_list = contacts.objects.filter(Q(userid = self.request.user),
            Q(contact_lastname__icontains=query )

            )
        
        return object_list

  