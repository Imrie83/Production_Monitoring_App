# Generated by Django 3.2.9 on 2021-12-09 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_alter_productsmodel_order_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componenttoolsmodel',
            name='machine_time',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='glasstoolmodel',
            name='machine_time',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
