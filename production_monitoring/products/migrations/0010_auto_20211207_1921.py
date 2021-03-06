# Generated by Django 3.2.9 on 2021-12-07 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20211207_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsmodel',
            name='frame_size',
        ),
        migrations.AddField(
            model_name='productsmodel',
            name='door_height',
            field=models.FloatField(default=0, verbose_name='Door width'),
        ),
        migrations.AddField(
            model_name='productsmodel',
            name='door_width',
            field=models.FloatField(default=0, verbose_name='Door width'),
        ),
        migrations.AlterField(
            model_name='componentsmodel',
            name='img',
            field=models.ImageField(null=True, upload_to='static/img/fixtures', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='customermodel',
            name='customer_email',
            field=models.EmailField(max_length=254, null=True, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='doorstylemodel',
            name='img',
            field=models.ImageField(upload_to='static/img/styles/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='glassmodel',
            name='img',
            field=models.ImageField(null=True, upload_to='static/img/glass/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='machining_time',
            field=models.IntegerField(editable=False, null=True, verbose_name='Total machining time'),
        ),
    ]
