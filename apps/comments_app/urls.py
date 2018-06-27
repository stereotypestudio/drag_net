from django.urls import path
from . import views

urlpatterns = [
	path('submit-comment', views.submitComment),
	path('delete-comment/<id>', views.deleteComment)
]