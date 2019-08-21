from django.urls import path
from shop.views import category, detail, add_to_cart

app_name = 'shop'

urlpatterns = [
    path('category/', category, name='category'),
    path('detail/<slug>/', detail, name='detail'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
]