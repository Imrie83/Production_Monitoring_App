# Generated by Django 3.2.9 on 2021-12-15 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_auto_20211215_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='componenttoolsmodel',
            old_name='component',
            new_name='component_id',
        ),
        migrations.RenameField(
            model_name='glasstoolmodel',
            old_name='glass',
            new_name='glass_id',
        ),
        migrations.RenameField(
            model_name='ordermodel',
            old_name='customer',
            new_name='customer_id',
        ),
        migrations.RenameField(
            model_name='productcomponent',
            old_name='component',
            new_name='component_id',
        ),
        migrations.RenameField(
            model_name='productcomponent',
            old_name='product',
            new_name='product_id',
        ),
    ]