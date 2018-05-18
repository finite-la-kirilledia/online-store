from django.shortcuts import render, redirect

from frontend.views import *


def add_review(request, book_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = Review(user=request.user, book=Book.objects.get(pk=book_id), text=request.POST['text'])
            review.save()

            return redirect('book_detail', book_id)

    else:
        return book_detail(request, book_id)


def add_comment(request, book_id, review_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment(user=request.user, review=Review.objects.get(pk=review_id), text=request.POST['text'])
            comment.save()

            return redirect('book_detail', book_id)

    else:
        return book_detail(request, book_id)
