from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileInfoForm


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Create a new user
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # Create a related UserProfileInfo instance
            profile = profile_form.save(commit=False)
            profile.user = user  # Link the profile to the user

            if 'profile_photo' in request.FILES:
                profile.profile_photo = request.FILES['profile_photo']
                profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'account/registeration.html', {'profile_form': profile_form, 'user_form': user_form, 'registered': registered})


def login(request):
    return render(request, 'account/login.html')
