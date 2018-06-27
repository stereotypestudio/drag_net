from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('login', views.login),
	path('register', views.register),
	path('logout', views.logout), 
	path('submitRegister', views.submitRegister),
	path('home', views.home),
	path('user', views.user),
	path('search', views.search),
	path('uploadPicture', views.uploadPicture)

]