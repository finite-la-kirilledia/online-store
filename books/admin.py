from django.contrib import admin

from .models import *


class BookImageInline(admin.TabularInline):
    model = BookImage
    extra = 0


class BookAuthorInline(admin.TabularInline):
    model = Book.authors.through
    extra = 0


class BookCategoryInline(admin.TabularInline):
    model = Book.categories.through
    extra = 0


class BookAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Book._meta.fields]
    inlines = [BookAuthorInline, BookCategoryInline, BookImageInline]

    exclude = ('authors', 'categories',)

    class Meta:
        model = Book


admin.site.register(Book, BookAdmin)

admin.site.register(BookStatus)
admin.site.register(BookImage)
admin.site.register(BookCategory)
admin.site.register(Country)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Comment)
admin.site.register(Review)
admin.site.register(Like)
