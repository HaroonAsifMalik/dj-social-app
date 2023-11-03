from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
# from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponse('The user is not active')
        else:
            return HttpResponse('No user found')

    return render(request, 'account/login.html', {})


def home(request):
    if request.user.is_authenticated:
        return HttpResponse('Welcome to the home page!')
    else:
        request.session['message'] = 'You need to be logged in to access the home page.'
        return redirect('user_login')


def user_logout(request):
    logout(request)
    return redirect('register')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_photo' in request.FILES:
                profile.profile_photo = request.FILES['profile_photo']
                profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'account/registration.html', {'profile_form': profile_form, 'user_form': user_form, 'registered': registered})
