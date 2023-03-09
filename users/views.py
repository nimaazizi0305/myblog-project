from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm,UserUpdatInfo,UserProfileUpdate
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.

# class register(CreateView):
#     form_class = UserCreationForm
#     template_name = "users/register.html"
#     success_url = reverse_lazy("home")


def register(request:HttpRequest):
    if request.method == "POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            messages.success(request,f"User {username} Created Now")
            return redirect("login")
    else:
        form=UserRegisterForm()
    context={
        "form":form
    }
    return render(request,"users/register.html",context)

@login_required(login_url="login")
def profile(request:HttpRequest):
    if request.method == "POST":
        user_info_form=UserUpdatInfo(request.POST,instance=request.user)
        user_profile_form=UserProfileUpdate(request.POST,request.FILES,instance=request.user.profile)

        if user_info_form.is_valid() and user_profile_form.is_valid():
            user_profile_form.save()
            user_info_form.save()
            messages.success(request,f"you're Profile changed")
            return redirect("profile")
    else:
        user_info_form=UserUpdatInfo(instance=request.user)
        user_profile_form=UserProfileUpdate()

    context={
        "user_info_form":user_info_form,
        "user_profile_form":user_profile_form
    }
    return render(request,"users/profile.html",context)









