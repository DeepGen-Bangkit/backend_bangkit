# Generated by Django 3.2.3 on 2021-06-02 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0010_recipe_estimated'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='kode',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
