from django.urls import path
from shop.views import category

app_name = 'shop'

urlpatterns = [
    path('category/', category, name='category')
]