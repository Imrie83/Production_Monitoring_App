# Generated by Django 3.2.9 on 2021-12-11 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0009_alter_toolsmodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='toolsmodel',
            name='total_run_time',
            field=models.IntegerField(default=0, editable=False, null=True),
        ),
    ]