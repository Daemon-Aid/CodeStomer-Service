from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

#paths arranged alphabetically by name
app_name = 'codeApp'
urlpatterns = [ 
    path('about', views.aboutView.as_view(), name="about_View"),
    path('admindash', views.admindashView.as_view(), name="admindash_View"),
    path('contact', views.contactView.as_view(), name="contact_View"),
    path('index', views.indexView.as_view(), name="index_View"),
    path('login', views.loginView.as_view(), name="login_View"),
    path('register', views.registerView.as_view(), name="register_View"),
    
    path('error', views.errorView.as_view(), name="error_View"),
    path('user', views.userView.as_view(), name="user_View"),
         
]
