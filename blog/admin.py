from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission



class BlogAdmin(admin.ModelAdmin):
	exclude = ['upload_date']

	# def save_model(self, request, obj, form, change):
	# 	# obj.author = request.user
	# 	super().save_model(request, obj, form, change)


admin.site.register(Blog, BlogAdmin)
