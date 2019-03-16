from django.shortcuts import render
from .models import farmer_user,rent_hire
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
import pandas as pd
from .plot_water import crop_yield
from django.urls import reverse
from django_tables2 import RequestConfig
# Create your views here.
def register(request):
	if request.method=='POST':
		farmer=farmer_user()
		farmer.farmer_reg_id=request.POST.get("farmerId")
		farmer.first_name=request.POST.get("firstname")
		farmer.last_name=request.POST.get("lastname")
		farmer.address=request.POST.get("address")
		farmer.district=request.POST.get("district")
		farmer.state=request.POST.get("state")
		farmer.age=request.POST.get("age")
		farmer.phone_no=request.POST.get("phone")
		if request.POST.get("pass")==request.POST.get("pass-confirm"):
			farmer.password=request.POST.get("pass")
			farmer.save()
			return HttpResponseRedirect('')
		else:
			messages.error(request,'password and confirm password not same!!!')
	else:
		return render(request,'portal/signup.html')


def login(request):
	if request.session.has_key('farmer_reg_id'):
		return HttpResponseRedirect('about_us')
	else:
		if request.method=='POST':
			farmer_reg_id=request.POST.get("username")
			password=request.POST.get("pass")
			authentication=farmer_user.objects.filter(farmer_reg_id=farmer_reg_id)
			for users in authentication:
				if(users.password==password):
					request.session['farmer_idno']=users.farmer_idno
					request.session['farmer_reg_id']=users.farmer_reg_id
					request.session['first_name']=users.first_name
					request.session['last_name']=users.last_name
					request.session['address']=users.address
					request.session['district']=users.district
					request.session['state']=users.state
					request.session['age']=users.age
					request.session['phone_no']=users.phone_no
					train=pd.read_csv('/home/sirzechlucifer/ML and ROS/e-Kisan/kisan_portal/portal/train.csv')
					crop_yield(train,request.session['district'])
					return HttpResponseRedirect('about_us')
				else:
					return render(request,'portal/login.html')
		else:
			return render(request,'portal/login.html')


def about_us(request):
	if request.session.has_key('farmer_reg_id'):
		return render(request,'portal/dashboard.html')
	else:
		return HttpResponseRedirect(reverse('login'))


def add_equipments(request):
	if request.session.has_key('farmer_reg_id'):
		if request.method=="POST":
			equipment=rent_hire()
			equipment.farmer_id_rent=farmer_user.objects.get(farmer_idno=request.session['farmer_idno'])
			equipment.equipment_name=request.POST.get('equipname')
			equipment.equipment_quantity=request.POST.get('quantity')
			equipment.owner_phoneno=request.session['phone_no']
			equipment.equipment_age=request.POST.get('usage')
			equipment.equipment_renting_price=request.POST.get('price')
			equipment.status_bit=False
			equipment.owner_district=request.session['district']
			equipment.owner_name=request.session['first_name']
			equipment.save()
		return render(request,'portal/addeq.html')
	else:
		return HttpResponseRedirect(reverse('login'))



def profile(request):
	if request.session.has_key('farmer_reg_id'):
		logged_in_user=farmer_user()
		logged_in_user.farmer_idno= request.session['farmer_idno']
		logged_in_user.farmer_reg_id=request.session['farmer_reg_id']
		logged_in_user.first_name=request.session['first_name']
		logged_in_user.last_name=request.session['last_name']
		logged_in_user.address=request.session['address']
		logged_in_user.district=request.session['district']
		logged_in_user.state=request.session['state']
		logged_in_user.age=request.session['age']
		logged_in_user.phone_no=request.session['phone_no']
		return render(request,'portal/profile.html',{'user':logged_in_user})
	else:
		return HttpResponseRedirect(reverse('login'))

def plant_predict(request):
	if request.session.has_key('farmer_reg_id'):
		return render(request,'portal/plant_predict.html')
	else:
		return HttpResponseRedirect(reverse('login'))


def water_predict(request):
	if request.session.has_key('farmer_reg_id'):
		return render(request,'portal/water_predict.html')
	else:
		return HttpResponseRedirect(reverse('login'))

def logout(request):
	try:
		del request.session['farmer_reg_id']
		del request.session['farmer_idno']
		del request.session['first_name']
		del request.session['last_name']
		del request.session['address']
		del request.session['district']
		del request.session['state']
		del request.session['age']
		del request.session['phone_no']
	except:
		pass
	return HttpResponseRedirect(reverse('login'))

def rent_equipments(request):
	if request.session.has_key('farmer_reg_id'):
		table=rent_hire.objects.filter(status_bit=False,owner_district=request.session['district']) 
		return render(request, 'portal/rent_equipments.html', {'rent_user': table})
	else:
		return HttpResponseRedirect(reverse('login'))

def yojna(request):
	if request.session.has_key('farmer_reg_id'):
		return render(request,'portal/yojna.html')
	else:
		return HttpResponseRedirect(reverse('login'))



def my_equipments(request):
	if request.session.has_key('farmer_reg_id'):
		if request.method=="POST":
			table=rent_hire.objects.filter(farmer_id_rent=request.session['farmer_idno'],status_bit=False)
			some_var = request.POST.get('list')
			indxs=some_var.split(',')
			count=0
			print(indxs)
			for x in table:
				if str(count) in indxs: 
					x.delete()
				count=count+1
			
			table1=rent_hire.objects.filter(farmer_id_rent=request.session['farmer_idno'],status_bit=False)
			return render(request,'portal/my_equipments.html',{'rent_user':table1})
		else:
			table=rent_hire.objects.filter(farmer_id_rent=request.session['farmer_idno'],status_bit=False)
			return render(request, 'portal/my_equipments.html', {'rent_user': table})
	else:
		return HttpResponseRedirect(reverse('login'))

