# Generated by Django 2.2.4 on 2019-08-18 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190815_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='author_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
