# Generated by Django 3.0.7 on 2020-06-27 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_map_app', '0005_auto_20200627_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='srid',
            field=models.FloatField(blank=True, default=4326, null=True),
        ),
    ]
