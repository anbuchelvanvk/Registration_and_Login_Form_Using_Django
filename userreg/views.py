from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=UserCreationForm()
    return render(request, "registration/registration.html",{'form':form})

def login(request):
    return render(request, "registration/login.html")

def logout(request):
    return render(request, "home.html")


