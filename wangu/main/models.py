from django.core.exceptions import ValidationError
from django.contrib.auth.models import User 
from django.urls import reverse
from django.db import models




# Create your models here.models.PositiveIntegerField(null=True, blank=True)



class contacts(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=100, blank=True, null=True)
    contact_lastname = models.CharField(max_length=100)
    contact_job = models.CharField(max_length=100,default='')
    contact_email = models.EmailField(max_length=100)
    contact_phone = models.PositiveIntegerField(unique= True)
    contact_address = models.CharField(max_length=100)
    contact_image = models.ImageField(default='default.jpg' ,upload_to ='profile_pics')

    class Meta:
        ordering =['contact_name']
    

    def __str__(self):
        return self.contact_lastname
    #after a creation or update the system will redirect to this url i.e detail view in this case
    def get_absolute_url(self):
        return reverse('view-contact',kwargs={'pk':self.pk})
    
    #this will validate the form to accept people form sunningdale only
    #fat models skinny view concept
    '''def clean(self):
        
        if self.contact_address != 'Sunningdale':
            raise ValidationError('we only want sunngindale people')   
        return self.clean_data'''
    
  