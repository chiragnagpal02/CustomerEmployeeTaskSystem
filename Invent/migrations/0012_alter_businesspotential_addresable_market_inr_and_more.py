# Generated by Django 4.0.6 on 2022-07-26 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invent', '0011_businesspotential_total_market_inr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesspotential',
            name='addresable_market_INR',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='businesspotential',
            name='potential',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='businesspotential',
            name='served_market_INR',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='businesspotential',
            name='total_market_INR',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]