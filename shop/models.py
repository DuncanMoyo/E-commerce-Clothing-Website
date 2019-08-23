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

    def get_add_to_cart_url(self):
        return reverse('shop:add-to-cart', kwargs={
            'slug': self.slug
        })

    def remove_from_cart_url(self):
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

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField()
    coupon = models.ForeignKey('Coupon', on_delete=models.CASCADE, blank=True, null=True )

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.IntegerField()

    def __str__(self):
        return self.code






















