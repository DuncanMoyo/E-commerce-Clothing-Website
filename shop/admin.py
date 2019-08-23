from django.contrib import admin
from shop.models import Item, Order, OrderItem, Coupon

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Coupon)

