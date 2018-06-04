from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext

from accounts.forms import UserLoginForm, UserCreationForm
from books.models import *
from books.forms import *


def index(request):
    context = {
        'books': Book.objects.all(),
        'booksImages': BookImage.objects.filter(is_main=True),
        'userLoginForm': UserLoginForm(),
        'userCreationForm': UserCreationForm()
    }

    return render(request, 'frontend/index.html', context)


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    likes = 0
    top_rated_review = book.review_set.first()
    for review in book.review_set.all():
        if review.comment_set.count() > likes:
            likes = review.comment_set.count()
            top_rated_review = review

    other_images = []
    for bookImage in book.bookimage_set.all():
        if bookImage.is_main == False:
            other_images.append(bookImage)

    context = {
        'userLoginForm': UserLoginForm(),
        'userCreationForm': UserCreationForm(),
        'book': book,
        'other_images': other_images,
        'top_rated_review': top_rated_review,
        'reviewForm': ReviewForm(),
        'commentForm': CommentForm(),
    }

    return render(request, 'frontend/book_detail.html', context)
