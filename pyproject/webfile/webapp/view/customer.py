from email import message
from django.db import models
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
from .booking import Booking


class Customer(models.Model):
    c_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s %s %s" % (self.c_id,self.first_name, self.last_name, self.email)

def Signup(request):
    if request.method == 'POST':
        # Assuming form fields are posted with names 'username', 'password', 'email', etc.
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        # Create a new user instance
        new_user = User.objects.create_user(username=username, email=email, password=password)
        
        # Add additional fields if necessary
        new_user.first_name = first_name
        new_user.last_name = last_name
        
        # Save the user to the database
        new_user.save()
        
        # Redirect to login page or any other page
        return render(request, 'login.html')
    elif request.method == 'GET':
        return render(request, 'Signup.html')
    else:
        return HttpResponse('error')
        
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            django_login(request, user)
            print("Login Success")
            return redirect('profile')  # Redirect to profile page upon successful login
        else:
            print("Invalid Username or Password")
            return render(request, "login.html", {'error': 'Invalid Username or Password'})
    else:
        return render(request, "login.html") 

def profile(request):
    if request.user.is_authenticated:
        user = request.user
        email = user.email if hasattr(user, 'email') else None
        package=Booking.objects.filter(user=user)
        profile_picture = user.profile.profile_picture if hasattr(user, 'profile') else None
        return render(request, "profile.html", {'user': user, 'email': email,'package':package, 'profile_picture': profile_picture})
    else:
        # Handle the case where the user is not authenticated (optional)
        return render(request, "login.html", {'error': 'Please log in to view your profile'})

def logout_view(request):
    logout(request)
    return redirect('index')

def isExists(self):
            if Customer.objects.filter(email=self.email):
                return True

            return False
