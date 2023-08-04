from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
# Create your views here.


def adminLogin(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'accountant/login.html')
    else:
        return render(request, 'accountant/login.html')


def adminLogout(request):
    logout(request)
    return redirect('/login/admin_login')


def register(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(sername=name, password=password,email=email)
        user.save()
        return redirect('/')
    else: 
        return render(request,'accountant/login.html')
    