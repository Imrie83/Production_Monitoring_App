# Generated by Django 3.2.9 on 2021-12-12 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0010_toolsmodel_total_run_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='toolsmodel',
            name='current_run_time',
            field=models.IntegerField(default=0, editable=False, null=True),
        ),
    ]
