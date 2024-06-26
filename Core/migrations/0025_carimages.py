# Generated by Django 4.2.9 on 2024-03-05 07:12

import cloudinary.models
import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0024_rename_overview_id_features_overview_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarImages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_by', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('updated_by', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('updated_date', models.DateTimeField(default=datetime.datetime.now)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('Image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('OverView', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.caroverview')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
