from django.contrib import admin

from .models import *


class OrderLineInline(admin.TabularInline):
    model = OrderLine
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [OrderLineInline]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class OrderLineAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderLine._meta.fields]

    class Meta:
        model = OrderLine


admin.site.register(OrderLine, OrderLineAdmin)

admin.site.register(OrderStatus)
