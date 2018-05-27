from django.db import models

from accounts.models import User
from books.models import Book


class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def is_in_basket(book_id):
        return book_id


class BasketElement(models.Model):
    basket = models.ForeignKey(Basket, default=None, blank=True, null=True, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, blank=True, null=True, default=None, on_delete=models.CASCADE)

    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.book.name, self.updated)

    def save(self, *args, **kwargs):
        self.price = self.book.price

        super(BasketElement, self).save(*args, **kwargs)


class OrderStatus(models.Model):
    name = models.CharField(max_length=225, blank=True, null=True, default=None)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Order statuses'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_status = models.ForeignKey(OrderStatus, blank=True, null=True, default=None, on_delete=models.SET_NULL)

    address = models.CharField(max_length=225, blank=True, null=True, default=None)
    total_price = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Заказ №{} - {}'.format(self.id, self.order_status)

    def save(self, *args, **kwargs):
        for order_element in self.orderelement_set.all():
            self.total_price += order_element.price

        super(Order, self).save(*args, **kwargs)


class OrderElement(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, blank=True, null=True, default=None, on_delete=models.SET_NULL)

    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.book, self.book)

    def save(self, *args, **kwargs):
        self.price = self.book.price

        super(OrderElement, self).save(*args, **kwargs)
