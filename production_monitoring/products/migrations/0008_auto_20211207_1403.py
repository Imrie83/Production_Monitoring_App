# Generated by Django 3.2.9 on 2021-12-07 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_productsmodel_glass'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='componentsmodel',
            options={'verbose_name': 'Component', 'verbose_name_plural': 'Components'},
        ),
        migrations.AlterModelOptions(
            name='customermodel',
            options={'verbose_name': 'Customer', 'verbose_name_plural': 'Customers'},
        ),
        migrations.AlterModelOptions(
            name='doorstylemodel',
            options={'verbose_name': 'Door Style', 'verbose_name_plural': 'Door Styles'},
        ),
        migrations.AlterModelOptions(
            name='glassmodel',
            options={'verbose_name': 'Glass', 'verbose_name_plural': 'Glass'},
        ),
        migrations.AlterModelOptions(
            name='productsmodel',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]
