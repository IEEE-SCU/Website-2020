"""IEEEwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views as blog_views
from . import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.home, name='home'),
    path('blogs/', blog_views.blogs, name='blogs'),
    # path('blogs/blog_detail/<int:blog_id>', blog_views.blog_detail, name='blog_detail'),
    path('blogs/user_blogs/<int:user_id>', blog_views.user_blogs, name='user_blogs'),
    # path('user/login/', auth_views.LoginView.as_view(template_name='user/login.html', redirect_authenticated_user=True), name='login'),
    # path('user/logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('add_blog/', blog_views.add_blog, name='add_blog'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)