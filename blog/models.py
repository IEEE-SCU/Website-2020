from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Author(models.Model):
	name = models.CharField(max_length=25)

	def __str__(self):
		return self.name

class Blog(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	# image = models.ImageField(upload_to='images/', blank=True)
	upload_date = models.DateTimeField(default=timezone.now)
	# author = models.ForeignKey(User, on_delete=models.CASCADE)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	image_src = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.title




	