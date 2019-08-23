from django.urls import path
from shop.views import (category, detail,
                        add_to_cart, BasketView,
                        remove_single_item_from_cart, remove_from_cart,
                        ItemDetailView)

app_name = 'shop'

urlpatterns = [
    path('category/', category, name='category'),
    path('detail/<slug>/', detail, name='detail'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('basket/', BasketView.as_view(), name='basket'),
    path('product/', ItemDetailView, name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
]