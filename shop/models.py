from django.db import models

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
    previous_post = models.ForeignKey('self', related_name='older', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='newer', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title












