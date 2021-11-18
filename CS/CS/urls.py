"""CS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include,path
from codeApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('codeApp/', include('codeApp.urls', namespace='codeApp')), 
    path('about', views.aboutView.as_view(), name="about_View"),
    path('admindash', views.admindashView.as_view(), name="admindash_View"),
    path('contact', views.contactView.as_view(), name="contact_View"),
    path('index', views.indexView.as_view(), name="index_View"),
    path('login', views.loginView.as_view(), name="login_View"),
    path('register', views.registerView.as_view(), name="register_View"),
    
    path('error', views.errorView.as_view(), name="error_View"),
    path('user', views.userView.as_view(), name="user_View"),
]
