from django.urls import path
from . import views

urlpatterns = [
	path('',views.login, name='login'),
    path('register', views.register, name='register'),
    path('about_us',views.about_us,name='about_us'),
    path('add_equipments',views.add_equipments,name='add_equipments'),
    path('profile',views.profile,name='profile')
]