# Generated by Django 3.2.9 on 2021-12-07 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211207_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsmodel',
            name='customer_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='products.customermodel'),
        ),
    ]
