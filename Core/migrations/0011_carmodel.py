# Generated by Django 4.2.9 on 2024-02-22 07:29

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0010_carbrand_remove_carmodel_carcompany_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_by', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('updated_by', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('updated_date', models.DateTimeField(default=datetime.datetime.now)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('Model_name', models.CharField(max_length=100)),
                ('Brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.carbrand')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
