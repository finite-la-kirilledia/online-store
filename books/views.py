from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect

from frontend.views import *


def add_review(request, book_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            rating = request.POST['rating']
            review = Review(user=request.user, book=Book.objects.get(pk=book_id), text=request.POST['text'],
                            rating=rating)

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


def is_liked(request):
    user_id = request.GET.get('user_id')
    review_id = request.GET.get('review_id')

    review = Review.objects.get(id=review_id)
    user = User.objects.get(id=user_id)

    like = Like.objects.filter(user=user, review=review)

    response = dict()
    if like:
        response['is_liked'] = True
    else:
        response['is_liked'] = False

    return JsonResponse(response)


def get_likes_count(request):
    review_id = request.GET.get('review_id')
    review = Review.objects.get(id=review_id)
    likes_count = review.like_set.count()

    response = dict()
    response['likes_count'] = likes_count

    return JsonResponse(response)


def like(request):
    user_id = request.GET.get('user_id')
    review_id = request.GET.get('review_id')

    review = Review.objects.get(id=review_id)
    user = User.objects.get(id=user_id)

    Like(user=user, review=review).save()

    return HttpResponse()
