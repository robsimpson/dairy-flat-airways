# Generated by Django 4.1 on 2023-06-05 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairy_flat_airways', '0026_flight_etd_origin_flight_flight_number_flight_plane_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='route_details',
            field=models.JSONField(max_length=254),
        ),
    ]
