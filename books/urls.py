from django.urls import path
from . import views

urlpatterns = [
    path('add_review/<int:book_id>', views.add_review, name='add_review'),
    path('add_review/<int:book_id>/<int:review_id>', views.add_comment, name='add_comment'),
    path('book/is_liked', views.is_liked, name='is_liked'),
    path('book/get_likes_count', views.get_likes_count, name='get_likes_count'),
    path('book/like', views.like, name='like'),
]
