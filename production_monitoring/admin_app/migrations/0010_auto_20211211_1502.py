# Generated by Django 3.2.9 on 2021-12-11 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_app', '0009_alter_employeemodel_section_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userproductmodel',
            name='prod_end',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Work ended'),
        ),
        migrations.AlterField(
            model_name='userproductmodel',
            name='prod_start',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Work started'),
        ),
    ]