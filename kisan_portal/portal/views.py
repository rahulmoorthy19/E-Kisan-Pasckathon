from django.shortcuts import render
from .models import farmer_user,rent_hire
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
import pandas as pd
from .plot_yield import crop_yield
from .plot_water import crop_water
from django.urls import reverse
# Create your views here.
logged_in_user=farmer_user()
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
			return HttpResponseRedirect('login')
		else:
			messages.error(request,'password and confirm password not same!!!')
	else:
		return render(request,'portal/signup.html')


def login(request):
	if request.session.has_key('username'):
		username = request.session['username']
		return HttpResponseRedirect('about_us')
	else:
		if request.method=='POST':
			farmer_reg_id=request.POST.get("username")
			password=request.POST.get("pass")
			authentication=farmer_user.objects.filter(farmer_reg_id=farmer_reg_id)
			for users in authentication:
				if(users.password==password):
					request.session['username'] = farmer_reg_id
					logged_in_user.farmer_idno=users.farmer_idno
					logged_in_user.farmer_reg_id=users.farmer_reg_id
					logged_in_user.first_name=users.first_name
					logged_in_user.last_name=users.last_name
					logged_in_user.address=users.address
					logged_in_user.district=users.district
					logged_in_user.state=users.state
					logged_in_user.age=users.age
					logged_in_user.phone_no=users.phone_no
					return HttpResponseRedirect('about_us')
				else:
					return render(request,'portal/login.html')
		else:
			return render(request,'portal/login.html')


def about_us(request):
	if request.session.has_key('username'):
		return render(request,'portal/dashboard.html')
	else:
		return HttpResponseRedirect(reverse('login'))


def add_equipments(request):
	if request.session.has_key('username'):
		if request.method=="POST":
			equipment=rent_hire()
			equipment.farmer_id_rent=farmer_user.objects.get(farmer_idno=logged_in_user.farmer_idno)
			equipment.equipment_name=request.POST.get('equipname')
			equipment.equipment_quantity=request.POST.get('quantity')
			equipment.equipment_company=request.POST.get('company')
			equipment.equipment_age=request.POST.get('usage')
			equipment.equipment_renting_price=request.POST.get('price')
			equipment.status_bit=1
			equipment.save()
		return render(request,'portal/addeq.html')
	else:
		return HttpResponseRedirect(reverse('login'))



def profile(request):
	if request.session.has_key('username'):
		return render(request,'portal/profile.html',{'user':logged_in_user})
	else:
		return HttpResponseRedirect(reverse('login'))

def plant_predict(request):
	if request.session.has_key('username'):
		train=pd.read_csv('/home/sirzechlucifer/ML and ROS/e-Kisan/kisan_portal/portal/train.csv')
		crop_yield(train,logged_in_user.district)
		return render(request,'portal/plant_predict.html')
	else:
		return HttpResponseRedirect(reverse('login'))


def water_predict(request):
	if request.session.has_key('username'):
		train=pd.read_csv('/home/sirzechlucifer/ML and ROS/e-Kisan/kisan_portal/portal/train.csv')
		crop_water(train,logged_in_user.district)
		return render(request,'portal/water_predict.html')
	else:
		return HttpResponseRedirect(reverse('login'))

def logout(request):
	try:
		del request.session['username']
	except:
		pass
	return HttpResponseRedirect(reverse('login'))


def yojna(request):
	if request.session.has_key('username'):
		return render(request,'portal/yojna.html')
	else:
		return HttpResponseRedirect(reverse('login'))
