# Generated by Django 3.2.9 on 2021-12-07 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0008_auto_20211207_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='section_id',
            field=models.ManyToManyField(related_name='employees', to='admin_app.DepartmentModel', verbose_name='Department name'),
        ),
    ]
