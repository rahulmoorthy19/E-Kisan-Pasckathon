from django.urls import path
from . import views

urlpatterns = [
	path('', views.login, name = 'login'),
    path('register', views.register, name='register'),
    path('about_us',views.about_us,name='about_us'),
    path('add_equipments',views.add_equipments,name='add_equipments'),
    path('profile',views.profile,name='profile'),
    path('plant_predict',views.plant_predict,name='plant_predict'),
    path('water_predict',views.water_predict,name='water_predict'),
    path('logout',views.logout,name='logout'),
    path('yojna',views.yojna,name='yojna'),
    path('rent_equipments',views.rent_equipments,name='rent_equipments'),
    path('my_equipments',views.my_equipments,name='my_equipments')
]
