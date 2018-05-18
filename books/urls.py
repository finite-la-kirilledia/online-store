from django.urls import path
from . import views

urlpatterns = [
    path('add_review/<int:book_id>', views.add_review, name='add_review'),
    path('add_review/<int:book_id>/<int:review_id>', views.add_comment, name='add_comment'),
]
