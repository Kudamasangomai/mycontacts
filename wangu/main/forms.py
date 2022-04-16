from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import contacts


class AddContactForm(forms.ModelForm):

    class Meta:
        model = contacts
        fields ='__all__'
        exclude = ['userid']