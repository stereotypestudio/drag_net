from django.shortcuts import render, redirect
from apps.users_app.models import *
from apps.comments_app.models import *
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.
def submitComment(request):
	queen = User.objects.get(id = request.session['queen'])

	content = request.POST['content']

	comment = Comment.objects.create(content = content, queen = queen)

	return JsonResponse(model_to_dict(comment))

	# return redirect('/user')

def deleteComment(request, id):
	comment = Comment.objects.get(id = id)

	queen = comment.queen

	comment.delete()

	return redirect('/user/'+str(queen.id))