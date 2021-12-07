# Generated by Django 3.2.9 on 2021-12-07 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_componentsmodel_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoorStyleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style_name', models.CharField(max_length=255, verbose_name='Style')),
                ('style_type', models.CharField(max_length=255, verbose_name='Door type')),
                ('img', models.ImageField(upload_to='', verbose_name='Image')),
            ],
        ),
        migrations.AddField(
            model_name='productsmodel',
            name='style',
            field=models.ForeignKey(default=None, on_delete=models.SET('None'), to='products.doorstylemodel', verbose_name='Door style'),
        ),
    ]
