# Generated by Django 4.0.5 on 2022-07-11 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Invent', '0006_alter_employee_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allottask',
            name='id_str',
        ),
    ]