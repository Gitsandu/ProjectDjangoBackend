# Generated by Django 4.2.9 on 2024-03-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0026_cardetails_fueltype_cardetails_seats_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='features',
            name='Transmission',
            field=models.CharField(default='', max_length=100),
        ),
    ]