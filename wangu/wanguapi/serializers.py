
from rest_framework.serializers import ModelSerializer #importing the serializers from the rest framework
from main.models import contacts #then import the model/databases you want to serialize/convert




class contactsSerializers(ModelSerializer):
    class Meta:
        model = contacts
        fields = '__all__'