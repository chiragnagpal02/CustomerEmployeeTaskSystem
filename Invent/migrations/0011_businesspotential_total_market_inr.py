# Generated by Django 4.0.6 on 2022-07-26 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invent', '0010_alter_businesspotential_addresable_market_inr_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesspotential',
            name='total_market_INR',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
    ]
