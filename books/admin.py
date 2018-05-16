from django.contrib import admin

from .models import *


class BookImageInline(admin.TabularInline):
    model = BookImage
    extra = 0


class BookAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Book._meta.fields]
    inlines = [BookImageInline]

    class Meta:
        model = Book


admin.site.register(Book, BookAdmin)

admin.site.register(BookStatus)
admin.site.register(BookImage)
