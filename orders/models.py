from django.db import models

from accounts.models import User
from books.models import Book


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
    order_status = models.ForeignKey(OrderStatus, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)

    address = models.CharField(max_length=225, blank=True, null=True, default=None)
    total_price = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Заказ №{} - {}'.format(self.id, self.order_status)

    def save(self, *args, **kwargs):
        for orderline in self.orderline_set.all():
            self.total_price += orderline.price_per_item

        super(Order, self).save(*args, **kwargs)


class OrderLine(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)

    price_per_item = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.book.name, self.book.price)

    def save(self, *args, **kwargs):
        self.price_per_item = self.book.price

        super(OrderLine, self).save(*args, **kwargs)
