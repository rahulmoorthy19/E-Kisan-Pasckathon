from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    ##path('login_page/',views.login, name='login')
]