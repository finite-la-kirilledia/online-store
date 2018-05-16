from django.shortcuts import render
from django.contrib.auth import authenticate, login as django_login, logout as django_logout

from .forms import UserLoginForm, UserCreationForm
from frontend.views import index


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            django_login(request, user)

            return index(request)

    form = UserLoginForm()
    context = {'form': form}

    return render(request, 'frontend/index.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            if user:
                django_login(request, user)

                return index(request)

    context = {
        'userLoginForm': UserLoginForm(),
        'userCreationForm': UserCreationForm()
    }

    return render(request, 'frontend/index.html', context)


def logout(request):
    django_logout(request)

    return index(request)
