# Generated by Django 3.2.9 on 2021-12-07 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_ordermodel_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componentsmodel',
            name='component_description',
            field=models.TextField(blank=True, null=True, verbose_name='Component description'),
        ),
        migrations.AlterField(
            model_name='componentsmodel',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/fixtures', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='componentsmodel',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Component name'),
        ),
        migrations.AlterField(
            model_name='componentsmodel',
            name='stock',
            field=models.IntegerField(default=0, verbose_name='Stock'),
        ),
        migrations.AlterField(
            model_name='customermodel',
            name='customer_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='customermodel',
            name='customer_phone',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Phone no.'),
        ),
        migrations.AlterField(
            model_name='glassmodel',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='glassmodel',
            name='glass_name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Glass name'),
        ),
        migrations.AlterField(
            model_name='glassmodel',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/glass/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='glassmodel',
            name='stock',
            field=models.IntegerField(default=0, verbose_name='In stock'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='order_number',
            field=models.CharField(default='JOB', help_text='order num. format - "JOB0000000"', max_length=20, unique=True, verbose_name='Order Num.'),
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='delivery_address',
            field=models.TextField(blank=True, null=True, verbose_name='Delivery address'),
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='delivery_date',
            field=models.DateField(blank=True, null=True, verbose_name='Delivery date'),
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='production_date',
            field=models.DateField(blank=True, null=True, verbose_name='Production date'),
        ),
    ]
