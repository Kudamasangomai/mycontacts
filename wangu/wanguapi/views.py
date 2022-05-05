from django.shortcuts import render
from requests import request
from rest_framework.response import Response
from rest_framework.decorators import api_view #describes the functionality i.e is it a get /post/put/delete
from main.models import contacts
from .serializers import contactsSerializers
from rest_framework import status


@api_view(['GET'])
def get_all(request):
		if request.method == 'GET':
				allcontacts = contacts.objects.all()
				serializedcontacts = contactsSerializers(allcontacts,many=True)
				return Response(serializedcontacts.data)
			
	

@api_view(['GET'])
def get_contact(request,id):
	single_contact = contacts.objects.get(pk=id)
	serializedcontact = contactsSerializers(single_contact,many=False)
	return Response(serializedcontact.data)


@api_view(['POST'])
def contact_create(request):
	serializer = contactsSerializers(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def contact_update(request,id):
		contact = contacts.objects.get(pk=id)
		serializer = contactsSerializers(instance=contact, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_contact(requet,id):
	contact = contacts.objects.get(pk=id)
	allcontacts = contacts.objects.all()
	serializedcontacts = contactsSerializers(allcontacts,many=True)
	contact.delete()	
	
	return Response("contact seccesfully deleted")
	#return Response(status=status.HTTP_204_NO_CONTENT)