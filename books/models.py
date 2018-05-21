from django.db import models

from accounts.models import User


class BookStatus(models.Model):
    name = models.CharField(max_length=225, blank=True, null=True, default=None)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Book statuses'


class BookCategory(models.Model):
    name = models.CharField(max_length=225, blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Book categories'


class Country(models.Model):
    name = models.CharField(max_length=225, blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'


class Author(models.Model):
    name = models.CharField(max_length=225, blank=True, null=True, default=None)
    bio = models.TextField(blank=True, null=True, default=None)
    birthday = models.DateField(blank=True, null=True, default=None)

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True, default=None)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=225, blank=True, null=True, default=None)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=225, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default=None)
    pages = models.IntegerField(blank=True, null=True, default=None)
    weight = models.IntegerField(blank=True, null=True, default=None)
    pub_year = models.IntegerField(blank=True, null=True, default=None)

    status = models.ForeignKey(BookStatus, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(BookCategory)
    publisher = models.ForeignKey(Publisher, blank=True, null=True, default=None, on_delete=models.SET_NULL)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '{} ${} - {}'.format(self.name, self.price, self.status)


class BookImage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='books_images/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.id, self.book.name)


class Review(models.Model):
    text = models.TextField(blank=True, null=True, default=None)
    rating = models.IntegerField(default=0, blank=True, null=True)
    likes = models.IntegerField(default=0, blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True, default=None)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    # def __str__(self):
    #     return '{} {}: {} - {}'.format(self.user.name, self.user.surname, self.text, self.updated)


class Comment(models.Model):
    text = models.TextField(blank=True, null=True, default=None)
    likes = models.IntegerField(default=0, blank=True, null=True)
    dislikes = models.IntegerField(default=0, blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, blank=True, null=True, default=None)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
