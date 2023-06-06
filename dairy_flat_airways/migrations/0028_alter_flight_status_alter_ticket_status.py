# Generated by Django 4.1 on 2023-06-05 10:39

import dairy_flat_airways.models
from django.db import migrations
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dairy_flat_airways', '0027_alter_flight_route_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='status',
            field=enumfields.fields.EnumField(default=0, enum=dairy_flat_airways.models.FlightStatus, max_length=10),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=enumfields.fields.EnumField(default=0, enum=dairy_flat_airways.models.TicketStatus, max_length=10),
        ),
    ]