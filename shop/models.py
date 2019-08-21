from django.db import models
from tinymce import HTMLField
from django.urls import reverse
from django.conf import settings

CATEGORY_CHOICES = (
    ('S', 'Shirts'),
    ('Sk', 'Skirts'),
    ('A', 'Accessories'),
    ('P', 'Pants'),
    ('T', 'T-shirts'),
)

GENDER_CHOICES = (
    ('M', 'Men'),
    ('L', 'Ladies'),
    ('K', 'Kids'),
)

BRAND_CHOICES = (
    ('A', 'Armani'),
    ('V', 'Versace'),
    ('J', 'Jack Honey'),
    ('C', 'Carlo Bruni'),
)

COLOR_CHOICES = (
    ('W', 'White'),
    ('B', 'Blue'),
    ('G', 'Green'),
    ('Y', 'Yellow'),
    ('R', 'Red'),
)


class Item(models.Model):
    title = models.CharField(max_length=120)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=GENDER_CHOICES, default='L', max_length=2)
    brand = models.CharField(choices=BRAND_CHOICES, default='A', max_length=2)
    color = models.CharField(choices=COLOR_CHOICES, default='W', max_length=2)
    slug = models.SlugField()
    image = models.ImageField()
    description = HTMLField(blank=True, null=True)
    previous_post = models.ForeignKey('self', related_name='older', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='newer', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:detail', kwargs={
            'slug': self.slug
        })

    def add_to_cart(self):
        return reverse('shop:add-to-cart', kwargs={
            'slug': self.slug
        })

    def remove_from_cart(self):
        return reverse('shop:remove-from-cart', kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.quantity} of {self.item.title}'


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)

    def __str__(self):
        return self.user.username

























