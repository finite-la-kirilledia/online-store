from django.shortcuts import render, get_object_or_404

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


def book_detail(request, book_id):
    context = {
        'userLoginForm': UserLoginForm(),
        'userCreationForm': UserCreationForm(),
        'book': get_object_or_404(Book, id=book_id),
    }

    return render(request, 'frontend/book_detail.html', context)
