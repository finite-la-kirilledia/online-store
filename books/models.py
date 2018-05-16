from django.db import models

from accounts.models import User


class BookStatus(models.Model):
    name = models.CharField(max_length=225)

    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Book statuses'


class Book(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default=None)
    publisher = models.CharField(max_length=225, blank=True, null=True, default=None)
    pages = models.IntegerField(blank=True, null=True, default=None)
    weight = models.IntegerField(blank=True, null=True, default=None)
    pub_year = models.DateTimeField(blank=True, null=True, default=None)
    book_status = models.ForeignKey(BookStatus, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)

    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.book_status)

    # class Meta:
    #     verbose_name = 'Книга'
    #     verbose_name_plural = 'Книги'


class BookImage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='books_images/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.id, self.book.name)

    # class Meta:
    #     verbose_name = 'Картинка'
    #     verbose_name_plural = 'Картинки'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    text = models.CharField(max_length=225)

    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
