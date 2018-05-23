from django.contrib import admin

from orders.models import *


class OrderElementInline(admin.TabularInline):
    model = OrderElement
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [OrderElementInline]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class OrderLineAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderElement._meta.fields]

    class Meta:
        model = OrderElement


admin.site.register(OrderElement, OrderLineAdmin)
admin.site.register(OrderStatus)


class BasketElementInline(admin.TabularInline):
    model = BasketElement
    extra = 0


class BasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Basket._meta.fields]
    inlines = [BasketElementInline]

    class Meta:
        model = Basket


admin.site.register(Basket, BasketAdmin)


class BasketLineAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BasketElement._meta.fields]

    class Meta:
        model = BasketElement


admin.site.register(BasketElement, BasketLineAdmin)
