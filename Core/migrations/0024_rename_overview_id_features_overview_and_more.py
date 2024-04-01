# Generated by Django 4.2.9 on 2024-03-03 15:57

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0023_features'),
    ]

    operations = [
        migrations.RenameField(
            model_name='features',
            old_name='OverView_Id',
            new_name='OverView',
        ),
        migrations.CreateModel(
            name='CarSpecification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_by', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('updated_by', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('updated_date', models.DateTimeField(default=datetime.datetime.now)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('mileage', models.CharField(max_length=50)),
                ('engine', models.CharField(max_length=50)),
                ('max_power', models.CharField(max_length=50)),
                ('torque', models.CharField(max_length=50)),
                ('seats', models.PositiveSmallIntegerField()),
                ('wheel', models.CharField(max_length=50)),
                ('engine_and_transmission', models.JSONField(default=dict)),
                ('dimensions_and_capacity', models.JSONField(default=dict)),
                ('miscellaneous', models.JSONField(default=dict)),
                ('OverView', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.caroverview')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]