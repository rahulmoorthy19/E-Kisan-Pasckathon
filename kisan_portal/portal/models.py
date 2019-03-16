from django.db import models
from django.conf import settings

class farmer_user(models.Model):
	farmer_idno=models.AutoField(primary_key=True)
	first_name=models.CharField(max_length=400,null=True,blank=False,default="rahul")
	last_name=models.CharField(max_length=400,null=True,blank=False,default="moorthy")
	address=models.CharField(max_length=100,null=True,blank=False,default="b302")
	district=models.CharField(max_length=100,null=True,blank=False,default="pune")
	state=models.CharField(max_length=100,null=True,blank=False,default="Maharashtra")
	age=models.IntegerField(null=True,blank=False,default=20)
	farmer_reg_id=models.CharField(max_length=100,null=True,blank=False,default="abcd")						##Kisan Registration ID
	phone_no=models.CharField(max_length=100,null=True,blank=False,default="8805979825")
	password=models.CharField(max_length=100,null=True,blank=False)

class rent_hire(models.Model):
	farmer_id_rent=models.ForeignKey(farmer_user,on_delete=models.CASCADE)
	equipment_name=models.CharField(max_length=100,null=False,blank=False)					##Mapping needs to be done in views.py along with drop down menu
	equipment_quantity=models.IntegerField(null=False,blank=False)	
	equipment_age=models.IntegerField(null=True,blank=True)
	equipment_renting_price=models.IntegerField(null=True,blank=True)
	owner_phoneno=models.CharField(max_length=100,null=True,blank=False,default="8805979825")	
	status_bit=models.BooleanField(null=False,blank=True,default=False)			##Availability check of equipment 0->not available 1->available
	owner_district=models.CharField(max_length=100,null=True,blank=False,default="pune")
	owner_name=models.CharField(max_length=400,null=True,blank=False,default="rahul")


