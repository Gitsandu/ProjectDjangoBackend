# Generated by Django 4.2.9 on 2024-03-03 07:05

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0022_caroverview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_by', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('updated_by', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('updated_date', models.DateTimeField(default=datetime.datetime.now)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('POWER_STEERING', models.BooleanField(default=False)),
                ('POWER_WINDOWS_FRONT', models.BooleanField(default=False)),
                ('AIR_CONDITIONER', models.BooleanField(default=False)),
                ('HEATER', models.BooleanField(default=False)),
                ('ADJUSTABLE_HEAD_LIGHTS', models.BooleanField(default=False)),
                ('FOG_LIGHTS_FRONT', models.BooleanField(default=False)),
                ('ANTI_LOCK_BRAKING_SYSTEM', models.BooleanField(default=False)),
                ('CENTRAL_LOCKING', models.BooleanField(default=False)),
                ('RADIO', models.BooleanField(default=False)),
                ('Entertainment_communication', models.JSONField(default=dict)),
                ('Safety', models.JSONField(default=dict)),
                ('Exterior', models.JSONField(default=dict)),
                ('Interior', models.JSONField(default=dict)),
                ('Comfort_convenience', models.JSONField(default=dict)),
                ('OverView_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.caroverview')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]