# Generated by Django 3.2.9 on 2021-12-09 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_alter_componentsmodel_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsmodel',
            name='order_num',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.ordermodel', verbose_name='Order number'),
        ),
    ]
