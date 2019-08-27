from django.urls import path
from shop.views import (category, detail,
                        add_to_cart, BasketView,
                        remove_single_item_from_cart, remove_from_cart,
                        ItemDetailView, CheckoutView,
                        RequestRefundView, PaymentView,
                        AddCouponView)

app_name = 'shop'

urlpatterns = [
    path('category/', category, name='category'),
    path('detail/<slug>/', detail, name='detail'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('basket/', BasketView.as_view(), name='basket'),
    path('product/', ItemDetailView.as_view(), name='product'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('checkout1/', CheckoutView.as_view(), name='checkout1'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
]