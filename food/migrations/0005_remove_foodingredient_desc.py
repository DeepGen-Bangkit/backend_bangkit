# Generated by Django 3.2.3 on 2021-05-31 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_auto_20210530_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodingredient',
            name='desc',
        ),
    ]
