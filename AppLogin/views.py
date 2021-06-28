from django.http.response import HttpResponse
from django.shortcuts import render, redirect


# Authentication

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


# Models & Forms

from .models import Profile
from .forms import ProfileForm, SignUpForm


# Messages

from django.contrib import messages




def signup(req):
    form = SignUpForm()

    if req.method == 'POST':
        form = SignUpForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, "Account created successfully. You can now login to your account.")
            return redirect('AppLogin:login')

    return render(req, 'AppLogin/sign_up.html', context={'title':'Sign Up', 'form':form})


def user_login(req):
    form = AuthenticationForm()

    if req.method == 'POST':
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req, user)
                return redirect('AppShop:home')

    return render(req, 'AppLogin/login.html', context={'title':'LogIn', 'form':form})


@login_required
def user_logout(req):
    logout(req)
    messages.warning(req, "You are logged out.")
    
    return redirect('AppLogin:signup')


@login_required
def user_profile(req):
    profile = Profile.objects.get(user=req.user)
    form = ProfileForm(instance=profile)

    if req.method == 'POST':
        form = ProfileForm(data=req.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(req, "Your profile information was updated successfully!")

    return render(req, 'AppLogin/change_profile.html', context={'form':form})