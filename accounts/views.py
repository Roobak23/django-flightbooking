from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please login.")
            return redirect("login")
    else:
        form = SignupForm()

    return render(request, "accounts/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid(): 
            user = form.get_user()
            login(request, user)
            return redirect('/')  

        else:
            
            return render(request, "accounts/login.html", {"form": form})

    else:
        form = AuthenticationForm()
        return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("/")
