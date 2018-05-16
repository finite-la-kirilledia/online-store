from django.db import models

from accounts.models import User
from books.models import Book


class OrderStatus(models.Model):
    name = models.CharField(max_length=225)

    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Order statuses'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_status = models.ForeignKey(OrderStatus, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=225, blank=True, null=True, default=None)

    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Заказ №{} - {}'.format(self.id, self.order_status)

    # class Meta:
    #     verbose_name = 'Заказ'
    #     verbose_name_plural = 'Заказы'


class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)

    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.book.name, self.book.price)

    # class Meta:
    #     verbose_name = 'Товар'
    #     verbose_name_plural = 'Товары'
