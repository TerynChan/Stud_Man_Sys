from django.http import HttpResponseRedirect
from django.shortcuts import render
from  django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Student
from django.contrib import messages
from .forms import SignUpForm, StudentForm


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        context = {
            'students'    : Student.objects.all(),
            'username'    : request.user.username.capitalize(),
            'user'        : request.user 
        }
        return render(request, 'student/index.html', context)
    else:
         return HttpResponseRedirect(reverse('login'))

def login_user(request):
    if request.method == 'POST':
        current_username = request.POST['username']
        current_password = request.POST['password']
        user = authenticate(request, username = current_username, password = current_password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        
        else:
            messages.success(request, 'Invalid Credentials... Try Again!!')
            return render(request, 'student/login.html')
    
    else:
        return render(request, 'student/login.html', {})

def logout_user(request):
   logout(request)
   messages.success(request, 'You have been logged out')
   return render(request, 'student/login.html')
    
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, 'You have been sucessfully registered')
            return HttpResponseRedirect(reverse('index'))
    else:
        form = SignUpForm()
        return render(request, 'student/register.html', {'form' : form} )

    return render(request, 'student/register.html', {'form' : form} )

def student_card(request, id):
    if request.user.is_authenticated:
        student = Student.objects.get(pk=id)
        return render(request, 'student/student_card.html', {'student' : student})
    else:
        messages.success(request, 'You must be logged in first....')
        return HttpResponseRedirect(reverse('index'))
    
def edit_student(request, id):
    if request.user.is_authenticated:
        current_student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, request.FILES, instance=current_student)
        if request.method == 'POST':
            if form.is_valid:
                form.save()
                messages.success(request, 'Record Successfully Editted....')
                return HttpResponseRedirect(reverse('index'))
            
        return render(request, 'student/edit_student.html', {'form':StudentForm(instance=current_student)})
    
    else:
        messages.success(request, 'You must be logged in first....')
        return HttpResponseRedirect(reverse('index'))
    
def delete_student(request, id):
    if request.user.is_authenticated:
        student = Student.objects.get(pk=id)
        student.delete()
        messages.success(request, 'Student Deleted Successfully....')
        return HttpResponseRedirect(reverse('index'))
    else:
        messages.success(request, 'You must be logged in first....')
        return HttpResponseRedirect(reverse('index'))

def add_student(request):
    form = StudentForm(request.POST, request.FILES)
    if request.user.is_authenticated:
        if request.method == 'POST':
                if form.is_valid():
                    new_student_number = form.cleaned_data['student_number']
                    new_image = form.cleaned_data['image']
                    new_first_name = form.cleaned_data['firstname']
                    new_last_name = form.cleaned_data['lastname']
                    new_email = form.cleaned_data['email']
                    new_program = form.cleaned_data['program']
                    

                new_student = Student(
                    student_number=new_student_number,
                    image=new_image,
                    firstname=new_first_name,
                    lastname=new_last_name,
                    email=new_email,
                    program=new_program,           
                )

                new_student.save()
                messages.success(request, 'Student Added Successfully')
                return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'student/add_student.html', {'form': StudentForm()})

    else:
        messages.success(request, 'You must be logged in first....')
        return HttpResponseRedirect(reverse('index'))
    
def search_student(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            student_number = request.POST['student_number']
            student = Student.objects.get(student_number = student_number)
            return render(request, 'student/search.html', {'student' : student})
 
    else:
        messages.success(request, 'You must be logged in first....')
        return HttpResponseRedirect(reverse('index'))        








 