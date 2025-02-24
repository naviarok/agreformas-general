# Generated by Django 5.0.7 on 2024-07-22 11:42

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversion',
            fields=[
                ('fullname', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=256, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('service', models.CharField(blank=True, choices=[('Apartment renovations', 'Apartment renovations'), ('kitchen renovations', 'kitchen renovations'), ('Bathroom renovations', 'Bathroom renovations'), ('Bathroom renovations', 'Bathroom renovations'), ('General renovations', 'General renovations'), ('Wood carpentry', 'Wood carpentry'), ('Aluminum carpentry', 'Aluminum carpentry'), ('Floors', 'Floors'), ('Plasterboard placement', 'Plasterboard placement')], default='Apartment renovations', max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
