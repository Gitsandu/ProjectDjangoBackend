# Generated by Django 4.2.9 on 2024-03-05 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0029_remove_cardetails_seats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardetails',
            name='FuelType',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cardetails',
            name='Transmission',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='caroverview',
            name='FuelType',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='caroverview',
            name='Seats',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='caroverview',
            name='Transmission',
            field=models.CharField(max_length=100),
        ),
    ]
