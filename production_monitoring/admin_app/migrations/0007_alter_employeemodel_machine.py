# Generated by Django 3.2.9 on 2021-12-07 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0006_machinemodel_machine_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='machine',
            field=models.ManyToManyField(editable=False, through='admin_app.MachineEmployeeModel', to='admin_app.MachineModel', verbose_name='Machine used'),
        ),
    ]