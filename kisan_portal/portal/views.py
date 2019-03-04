from django.shortcuts import render
from .models import farmer_details,rent_details
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def register(request):
	if request.method=='POST':
		farmer=farmer_details()
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
			return render(request, 'portal/signup.html')

	else:
		return render(request,'portal/signup.html')


def login(request):
	if request.method=='POST':
		farmer_reg_id=request.POST.get("username")
		password=request.POST.get("pass")
		authentication=farmer_details.objects.filter(farmer_reg_id=farmer_reg_id)
		for users in authentication:
			if(users.password==password):
				return HttpResponseRedirect('home/')
			else:
				return render(request,'portal/login.html')
	else:
		return render(request,'portal/login.html')


def home(request):
	return render(request,'portal/dashboard.html')
