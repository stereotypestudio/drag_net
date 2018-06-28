from django.urls import path
from . import views

urlpatterns = [
	path('submitEvent/<queen>', views.submitEvent),
	path('deleteEvent/<id>', views.deleteEvent)
]