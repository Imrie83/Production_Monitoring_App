# Generated by Django 3.2.9 on 2021-12-15 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_rename_customer_id_ordermodel_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='componenttoolsmodel',
            old_name='component_id',
            new_name='component',
        ),
        migrations.RenameField(
            model_name='glasstoolmodel',
            old_name='glass_id',
            new_name='glass',
        ),
        migrations.RenameField(
            model_name='productcomponent',
            old_name='component_id',
            new_name='component',
        ),
        migrations.RenameField(
            model_name='productcomponent',
            old_name='product_id',
            new_name='product',
        ),
    ]
