from django.shortcuts import render, redirect
from apps.users_app.models import *
from apps.comments_app.models import *

# Create your views here.
def submitComment(request):
	queen = User.objects.get(id = request.session['queen'])

	content = request.POST['content']

	Comment.objects.create(content = content, queen = queen)

	return redirect('/user')

def deleteComment(request, id):
	pass