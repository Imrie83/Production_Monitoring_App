# Generated by Django 3.2.9 on 2021-12-07 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0005_alter_toolsmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toolsmodel',
            name='max_run_time',
            field=models.IntegerField(help_text='Maximum run time allowed before tool change - in minutes!', null=True, verbose_name='Allowed run time'),
        ),
        migrations.AlterField(
            model_name='toolsmodel',
            name='tool_name',
            field=models.CharField(help_text='Short tool name', max_length=255, verbose_name='Tool name'),
        ),
        migrations.AlterField(
            model_name='toolsmodel',
            name='type',
            field=models.CharField(help_text='PCD - HSS - Carbide', max_length=255, null=True, verbose_name='Type'),
        ),
    ]