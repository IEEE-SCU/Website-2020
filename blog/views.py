from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .forms import AddBlogForm

def home(request):
	return render(request, 'blog/home.html')

def blogs(request):
	blogs = Blog.objects.all().order_by('-upload_date')
	paginator = Paginator(blogs, 5)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	num_blogs = len(blogs)
	return render(request, 'blog/blogs.html', {'num_blogs': num_blogs, 'page_obj': page_obj})

def blog_detail(request, blog_id):
	blog = Blog.objects.get(pk=blog_id)
	return render(request, 'blog/blog_detail.html', {'blog': blog})

def user_blogs(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	blogs = Blog.objects.filter(author=user)
	paginator = Paginator(blogs, 5)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	num_blogs = len(blogs)
	return render(request, 'blog/user_blogs.html', {'num_blogs': num_blogs, 'user': user, 'page_obj': page_obj})

def add_blog(request):
	form = AddBlogForm()

	if request.method == 'POST':
		form = AddBlogForm(request.POST, request.FILES)
		if form.is_valid():
			form.instance.author = request.user
			form.save()
			return redirect('home')
	return render(request, 'blog/add_blog.html', {'form': form})