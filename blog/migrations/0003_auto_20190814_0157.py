# Generated by Django 2.2.4 on 2019-08-13 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190814_0148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='user',
        ),
    ]