from django.db import models
from apps.users_app.models import *

# Create your models here.
class Comment(models.Model):
	content = models.TextField()
	queen = models.ForeignKey(User, related_name = "comments", on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now_add = True)