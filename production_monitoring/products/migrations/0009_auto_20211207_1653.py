# Generated by Django 3.2.9 on 2021-12-07 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20211207_1403'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='componenttoolsmodel',
            options={'verbose_name': 'Component Tool', 'verbose_name_plural': 'Component Tools'},
        ),
        migrations.AlterModelOptions(
            name='glasstoolmodel',
            options={'verbose_name': 'Aperture Tool', 'verbose_name_plural': 'Aperture Tools'},
        ),
    ]