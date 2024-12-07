from django.shortcuts import render
#from .models import Customer
from .view.customer import Customer
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# Create your views here.
def event(request):
    return render(request,'event.html')
def index(request):
    return render(request,'index.html')
def four(request):
    return render(request,'404.html')
def about(request):
    return render(request,'about.html')
def blog(request):
    return render(request,'blog.html')

def profile(request):

    cust=Customer.objects.all()
    context ={
        'cust':cust
    }
    print(context)
    return render(request,'profile.html',context)
def book(request):
    return render(request,'book.html')
def contact(request):
    return render(request,'contact.html')
# def menu(request):
#     return render(request,'menu.html')
# def Signup(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password = request.POST['password']
#         phone_number = request.POST['phone_number']
#         date_of_birth = request.POST['date_of_birth']
#         gender = request.POST['gender']
#         username = request.POST['username']
#
#         new_cust=Customer(first_name=first_name,last_name=last_name,email=email,password=password,phone_number=phone_number,date_of_birth=date_of_birth,gender=gender,username=username)
#         new_cust.save()
#         return HttpResponse('Customer added succesfull')
#     elif request.method == 'GET':
#         return render(request,'Signup.html')
#     else:
#         return HttpResponse('error ')
#
# def login(request):
#     if request.method == "POST":
#         new_cust = Customer.objects.filter(username=request.POST['username'],password=request.POST['password'])
#         if new_cust:
#             print("Login Success")
#             return render(request, "index.html")
#         else:
#             print("Invalid Username or Password")
#             return render(request, "login.html")
#     else:
#         return render(request, "login.html")
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     customer=authenticate(username=username,password=password)
    #     if customer is not None:
    #         login(request,customer)
    #         return HttpResponse('login succesfull')
    # return render(request,'login.html')
def service(request):
    return render(request,'service.html')
def team(request):
    return render(request,'team.html')
def testimonial(request):
    return render(request,'testimonial.html')