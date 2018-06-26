from django.db import models
import re
# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
LETTERS_ONLY_REGEX = re.compile(r'^[a-zA-Z]+$')
class UserManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['dragName']) < 1 or len(postData['houseName']) < 1:
			errors['name'] = "Names must be at least 3 letters long"
		elif not LETTERS_ONLY_REGEX.match(postData['dragName']) or not LETTERS_ONLY_REGEX.match(postData['houseName']):
			errors['name'] = "Names must be letters only"
		elif not EMAIL_REGEX.match(postData['email']):
			errors['email'] = "Must be a valid email"
		elif len(postData['email']) < 1:
			errors['email'] = "Email can't be blank"
		elif len(User.objects.filter(email = postData['email'])) > 0:
			errors['email'] = "Email exists"
		elif postData['password'] != postData['confirm-pw']:
			errors['password'] = "Passwords must match"
		elif len(postData['password']) < 8:
			errors['password'] = "Passwords must be at least 8 characters match"

		return errors

	def login_validator(self, postData):
		errors = {}
		if not EMAIL_REGEX.match(postData['email']):
			errors['email'] = "Must be a valid email"

		return errors


class User(models.Model):
	dragName = models.CharField(max_length = 255)
	houseName = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	password_hash = models.CharField(max_length = 255)

	objects = UserManager()