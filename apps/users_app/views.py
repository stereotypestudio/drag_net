from django.shortcuts import render, redirect
from apps.users_app.models import *
from apps.comments_app.models import *
from apps.events_app.models import *
from django.contrib import messages
from django.template.context_processors import csrf
from .forms import UploadFileForm
import bcrypt

# Create your views here.
def index(request):

	args = {}
	args.update(csrf(request))

	return render(request, "index.html", args)

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

def uploadPicture(request):
	user = User.objects.get(id = request.session['user'])
	user.profile_image = request.FILES.get('profile-picture')
	user.save()

	return redirect('/home')

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
	print(user)

	return render(request, 'home.html', {'user' : user})

def user(request):

	queen = User.objects.first()
	request.session['queen'] = queen.id
	comments = Comment.objects.filter(queen = queen)
	events = Event.objects.filter(queen = queen)

	for key in request.session.keys():
		print(request.session[key])

	return render(request, "user.html", {'queen' : queen, 'comments' : comments, 'events': events})

# def search(request):
# 	print('Search function')
# 	if request.method == 'POST':
# 		search_text = request.post['search-text']
# 	else:
# 		search_text = " "

# 	queens = User.objects.filter(dragName__contains=search_text)

# 	return render("ajax_search.html", {"queens" : queens})

def search(request):
	if request.is_ajax():
		q = request.GET.get('q')
		if q is not None:            
			results = User.objects.filter(dragName__startswith = q)        
			return render(request, 'results.html', {'results': results})
