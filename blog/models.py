from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Blog(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	# image = models.ImageField(upload_to='images/', blank=True)
	upload_date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title



	