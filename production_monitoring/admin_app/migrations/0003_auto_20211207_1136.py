# Generated by Django 3.2.9 on 2021-12-07 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0002_auto_20211207_1007'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sectionmodels',
            options={'verbose_name_plural': 'Sections'},
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='id_num',
            field=models.IntegerField(default=None, verbose_name='Employee id number'),
        ),
    ]
