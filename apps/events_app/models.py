from django.db import models
from apps.users_app.models import *

# Create your models here.
class Event(models.Model):
	location = models.CharField(max_length = 255)
	address = models.CharField(max_length = 255)
	dateTime = models.DateTimeField()
	desc = models.TextField()
	queen = models.ForeignKey(User, related_name = "events", on_delete = models.CASCADE)