from django import forms
from .models import Blog

class AddBlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		exclude = ['author', 'upload_date']