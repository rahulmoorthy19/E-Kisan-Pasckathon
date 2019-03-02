from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class farmer_details(models.Model):
	farmer_id=models.ForeignKey(User,on_delete_cascade=True)					##Uinque Id for farmers which is useful for renting
	first_name=models.CharField(max_length=400,null=False,blank=False)
	last_name=models.CharField(max_length=400,null=False,blank=False)
	address=models.CharField(max_length=100,null=False,blank=False)
	district=models.CharField(max_length=100,null=False,blank=False)
	state=models.CharField(max_length=100,null=False,blank=False)
	taluka=models.CharField(max_length=100,null=False,blank=False)
	age=models.IntegerField(null=False,blank=False)
	farmer_reg_id=models.CharField(max_length=100,null=False,blank=False)						##Kisan Registration ID
	phone_no=model.CharField(max_length=100,null=False,blank=False)

class rent_details(models.Model):
	farmer_id=models.ForeignKey(farmer_details,on_delete_cascade=True)
	equipment_name=models.IntegerField(null=False,blank=False)					##Mapping needs to be done in views.py along with drop down menu
	equipment_quantity=models.IntegerField(null=False,blank=False)		
	status_bit=models.IntegerField(null=False,blank=True)						##Availability check of equipment


