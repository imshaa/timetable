from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match!")
            # return HttpResponse("Your password doesn't match !")
        else:
            if User.objects.filter(username=uname).exists():
                messages.error(request, "Username already exists!")
                return redirect('register')
            my_user = User.objects.create_user(username=uname, email=email, password=pass1)
            my_user.save()
            messages.success(request, "Registered successfully! Try logging in.")

            return redirect('loginpage')

      
    return render(request, 'register.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        
        else:
            messages.error(request, "Wrong username or password. Try again.")
            return redirect('loginpage')
    return render(request, 'login.html')

def logoutpage(request):
    logout(request)
    return redirect('loginpage')
