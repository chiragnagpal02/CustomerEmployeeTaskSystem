# Generated by Django 4.0.5 on 2022-07-05 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='id',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='customer',
            name='fleet_categorization',
            field=models.CharField(choices=[('ISV-In UDI-Not in SFDC', 'ISV-In UDI-Not in SFDC'), ('ISV-In SFDC-In UDI-Retain', 'ISV-In SFDC-In UDI-Retain'), ('GSV-Matching with SFDC', 'GSV-Matching with SFDC'), ('GSV-Not in SFDCs', 'GSV-Not in SFDCs'), ('GSV-Not in UDI', 'GSV-Not in UDI')], max_length=400),
        ),
    ]