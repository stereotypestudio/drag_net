from django.shortcuts import render, redirect
from apps.users_app.models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):

	return render(request, "index.html")

def login(request):
	errors = User.objects.login_validator(request.POST)
	if len(errors):
		for key, value in errors.items():
			messages.error(request, value)
			return redirect('/')
	else:	
		user = User.objects.get(email=request.POST['email'])

		if bcrypt.checkpw(request.POST['password'].encode(), user.password_hash.encode()):
			if "user" not in request.session:
				request.session['user'] = user.id
			else:
				request.session['user'] = user.id
			return redirect('/home')
		else:
			return redirect('/')

def logout(request):

	request.session.clear()

	return redirect('/')

def register(request):

	return render(request, 'register.html')

def submitRegister(request):

	dragName = request.POST['dragName']
	houseName = request.POST['houseName']
	email = request.POST['email']
	password_hash  = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

	user = User.objects.create(dragName = dragName, houseName = houseName, email = email, password_hash = password_hash)

	request.session['user'] = user.id

	return redirect('/home')


def home(request):

	user = User.objects.get(id = request.session['user'])

	return render(request, 'home.html', {'user' : user})