# Generated by Django 4.2.9 on 2024-02-22 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0011_carmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='Brand_id',
            new_name='Brand',
        ),
    ]
