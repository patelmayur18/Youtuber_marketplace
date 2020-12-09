from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import  messages,auth
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    return render(request,'accounts/dashboard.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are login sucsesfully')
            return redirect('dashboard')
        else:
            messages.warning(request,'You have enterd invalid data')
            return redirect('login')

    return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request,'Username already exist')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request,'You have already registed your mail id')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name= firstname,last_name = lastname,username=username,password=password,email=email)
                    user.save()
                    messages.success(request,'You are successfully registed')  
                    return redirect('login')  

    return render(request,'accounts/register.html') 

def logout(request):
    auth.logout(request)
    messages.success(request,'You have logout from your account')
    return redirect('login')          