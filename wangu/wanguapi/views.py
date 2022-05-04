from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import contacts
from .serializers import contactsSerializers

# Create your views here.

    #get all the contacts
  

@api_view(['GET'])
def get_all(request):
	allcontacts = contacts.objects.all()
	serializedcontacts = contactsSerializers(allcontacts,many=True)
	return Response(serializedcontacts.data)