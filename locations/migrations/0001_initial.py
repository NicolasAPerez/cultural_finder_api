# Generated by Django 5.0.7 on 2024-07-19 00:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=90)),
                ('city', models.CharField(max_length=45)),
                ('picture', models.URLField(blank=True, default='https://d21x6gt1bw5dh5.cloudfront.net/building1.jpg')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_stars', models.PositiveSmallIntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.location')),
            ],
        ),
    ]
