from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Student

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
	username = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'User Name'}))
	password1 = forms.CharField(label='', max_length=100,help_text='must be at 8 characters including letters and digits', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
	password2 = forms.CharField(label='', max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
          
	
class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['student_number','image', 'firstname', 'lastname', 'email', 'program']
    labels = {
      'student_number': '',
      'image': '',
      'firstname': '',
      'lastname': '',
      'email': '',
      'program': '', 
    }
    
    widgets = {
      'student_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Student Number',}),
      'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder':'Picture',}),
      'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name',}),
      'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Student Last Name',}),
      'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Student Email',}),
      'program': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Program',}),
    }