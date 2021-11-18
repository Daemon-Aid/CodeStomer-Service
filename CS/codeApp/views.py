from collections import namedtuple
from django.db.models.fields import EmailField
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class aboutView(View):
    def get(self, request):
        return render(request, 'about.html',{})


# Admin Dashboard View
class admindashView(View):
    def get(self, request):
        contact = Contact.objects.all()
        error = Error.objects.all()
        user = User.objects.all()
        agent = Agent.objects.all()
        context = {
            'contact' : contact,
            'error' : error,
            'user' : user,
            'agent' : agent
        }

        return render(request, 'admindash.html', context)
    def post(self, request):
        if request.method == 'POST':
            if 'contactDeleteBtn' in request.POST: # LABIAGA CONTACT DELETE
                contactID = request.POST.get("contactDel")
                contactDelete = Contact.objects.filter(contactID = contactID).delete()
                print('recorded deleted')

            elif 'contactUpdateBtn' in request.POST: # LABIAGA CONTACT UPDATE
                contactID = request.POST.get("contactID")
                name = request.POST.get("name")
                email = request.POST.get("email") 
                subject = request.POST.get("subject")
                message = request.POST.get("message")
                contactUpdate = Contact.objects.filter(contactID = contactID).update(name = name, email = email, subject = subject, message = message)

            elif 'errorDeleteBtn' in request.POST: # CABAHUG ERROR DELETE
                errorID = request.POST.get("errorDel")
                errorDelete = Error.objects.filter(errorID = errorID).delete()
                print('recorded deleted')

            elif 'errorUpdateBtn' in request.POST: # CABAHUG ERROR UPDATE
                errorID = request.POST.get("errorID")
                message = request.POST.get("message")
                code = request.POST.get("code") 
                explination = request.POST.get("explination")
                fix = request.POST.get("fix")
                errorUpdate = Error.objects.filter(errorID = errorID).update(message = message, code = code, explination = explination, fix = fix)

            elif 'userDeleteBtn' in request.POST: # POCONG USER DELETE
                userID = request.POST.get("userDel")
                errorDelete = User.objects.filter(userID = userID).delete()
                print('recorded deleted') 

            elif 'userUpdateBtn' in request.POST: # POCONG USER UPDATE 
                userID = request.POST.get("userID")
                firstname = request.POST.get("firstname")
                lastname = request.POST.get("lastname") 
                course = request.POST.get("course")
                year = request.POST.get("year")
                email = request.POST.get("email")
                userUpdate = User.objects.filter(userID = userID).update(firstname = firstname, lastname = lastname, course = course, year = year, email = email)          
        return redirect('codeApp:admindash_View')
  
		

# Contact Add
class contactView(View):
    def get(self, request):
        context = {}
        return render(request, 'contact.html',context)
    def post(self, request):
        form = ContactForm(request.POST)
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        print(message)
        form = Contact(
                name = name,
                email = email,
                subject = subject,
                message = message
        )
        form.save()
        return redirect('codeApp:contact_View')

class errorView(View):
    def get(self, request):
        context = {}
        return render(request, 'error.html',context)    
    def post(self, request):
        form = ErrorForm(request.POST)
        message = request.POST.get("message")
        code = request.POST.get("code")
        print(message)
        form = Error(
                message = message,
                code = code
        )
        form.save()
        return redirect('codeApp:error_View')

class userView(View):
    def get(self, request):
        return render(request, 'user.html',{})
    def post(self, request):
        form = UserForm(request.POST)
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        course = request.POST.get("course")
        year = request.POST.get("year")
        email = request.POST.get("email")
        print(firstname)
        form = User(
                firstname = firstname,
                lastname = lastname,
                course = course,
                year = year,
                email = email,
        )
        form.save()
        return redirect('codeApp:user_View')    
    

class indexView(View):
    def get(self, request):
        return render(request, 'index.html',{})

class loginView(View):
    def get(self, request):
        return render(request, 'login.html',{})

class registerView(View):
    def get(self, request):
        return render(request, 'register.html',{})

