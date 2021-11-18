from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields= '__all__'

class ErrorForm(forms.ModelForm):
	class Meta:
		model = Error
		fields= '__all__'

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields= '__all__'

class AgentForm(UserCreationForm):
    firstname = forms.CharField(max_length= 100)
    lastname = forms.CharField(max_length= 100)
    phone_number = forms.CharField(max_length=11)
    email = forms.CharField(max_length=100)
    class Meta:
        model = Agent
        fields =  ('firstname', 'lastname', 'phone_number', 'email', 'username', 'password1', 'password2' )



