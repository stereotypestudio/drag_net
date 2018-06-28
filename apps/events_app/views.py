from django.shortcuts import render, redirect
from apps.users_app.models import *
from apps.events_app.models import *

# Create your views here.
def submitEvent(request, queen):
	queen = User.objects.get(id = queen)

	location = request.POST['location']
	address = request.POST['address']
	dateTime = request.POST['dateTime']
	desc = request.POST['desc']

	Event.objects.create(location = location, address = address, dateTime = dateTime, desc = desc, queen = queen)

	return redirect('/home')


def deleteEvent(request, id):
	event = Event.objects.get(id = id)

	queen = event.queen

	event.delete()

	return redirect("/user/" + str(queen.id))
