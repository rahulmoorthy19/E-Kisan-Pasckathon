from django.shortcuts import render
from .models import farmer_details,rent_details
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
farmer=farmer_details()
def register(request):
	if request.method=='POST':
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
			return HttpResponseRedirect('login_page/')
		else:
			return render(request, 'portal/signup.html')

	else:
		return render(request,'portal/signup.html')
