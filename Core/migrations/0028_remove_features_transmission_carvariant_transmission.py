# Generated by Django 4.2.9 on 2024-03-05 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0027_features_transmission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='features',
            name='Transmission',
        ),
        migrations.AddField(
            model_name='carvariant',
            name='Transmission',
            field=models.CharField(default='', max_length=100),
        ),
    ]