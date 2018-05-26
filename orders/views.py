from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from orders.models import *
from orders.forms import CheckboxForm


def add_to_basket(request):
    book_id = request.POST.get('book_id')
    user_id = request.POST.get('user_id')

    user = User.objects.get(id=user_id)
    book = Book.objects.get(id=book_id)

    basket, created = Basket.objects.get_or_create(user=user)
    basket.save()
    basket_element = BasketElement(basket=basket, book=book)
    basket_element.save()

    return HttpResponse()


def checkout(request, user_id):
    basket = User.objects.get(id=user_id).basket

    books = []
    for item in basket.basketelement_set.all():
        books.append(item.book)

    checkboxForm = CheckboxForm()

    return render(request, 'frontend/checkout.html', locals())


def delete_from_basket(request, user_id, book_id):
    basket = User.objects.get(id=user_id).basket
    basket.basketelement_set.get(book=Book.objects.get(id=book_id)).delete()

    return checkout(request, user_id)


def is_in_basket(request):
    book_id = request.GET.get('book_id')
    user_id = request.GET.get('user_id')

    user = User.objects.get(id=user_id)
    book = Book.objects.get(id=book_id)
    basket = user.basket

    response = dict()
    for item in basket.basketelement_set.all():
        if item.book == book:
            response['is_in_basket'] = True
        else:
            response['is_in_basket'] = False

    return JsonResponse(response)


def delete_book_from_basket(request):
    basket = User.objects.get(id=request.GET.get('user_id')).basket
    book = Book.objects.get(id=request.GET.get('book_id'))

    for basketelement in basket.basketelement_set.all():
        if basketelement.book == book:
            basketelement.delete()

    return HttpResponse()
