# Generated by Django 3.2.9 on 2021-12-07 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20211207_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsmodel',
            name='glass',
            field=models.ForeignKey(default=None, on_delete=models.SET('None'), to='products.glassmodel', verbose_name='Glass'),
        ),
    ]
