from django.db import models
from django.contrib.auth import get_user_model
from tinymce import HTMLField

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    category = models.ManyToManyField(Category)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0, null=True, blank=True)
    thumbnail = models.ImageField()
    overview = models.CharField(max_length=200)
    content = HTMLField('Content')
    featured = models.BooleanField(default=True)
    previous_post = models.ForeignKey('self', related_name='older', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='newer', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title


