# Generated by Django 3.2.9 on 2021-12-08 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20211208_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componentsmodel',
            name='product_type',
            field=models.CharField(choices=[('lock', 'Lock'), ('handle', 'Handle'), ('viewer', 'Viewer'), ('knocker', 'Knocker'), ('letter plate', 'Letter plate'), ('hinges', 'Hinges'), ('apertures', 'Apertures'), ('numerals', 'Numerals')], default=('lock', 'Lock'), max_length=255, verbose_name='Type'),
        ),
    ]