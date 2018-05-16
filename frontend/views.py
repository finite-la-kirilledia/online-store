from django.shortcuts import render

from accounts.forms import UserLoginForm, UserCreationForm
from books.models import *


def index(request):
    context = {
        'books': Book.objects.all(),
        'booksImages': BookImage.objects.filter(is_main=True),
        'userLoginForm': UserLoginForm(),
        'userCreationForm': UserCreationForm()
    }

    return render(request, 'frontend/index.html', context)
