from rest_framework import serializers # importing the serializers from the rest framework
from main.models import contacts #then import the model you want to serialize




class contactsSerializers(serializers.ModelSerializer):
    class Meta:
        model = contacts
        fields = '__all__'