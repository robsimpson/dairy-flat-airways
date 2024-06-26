# Generated by Django 4.1 on 2023-06-05 08:28

import dairy_flat_airways.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairy_flat_airways', '0022_schedule_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='stage',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='flight',
            name='status',
            field=models.CharField(choices=[(dairy_flat_airways.models.FlightStatus['SCHEDULED'], 0), (dairy_flat_airways.models.FlightStatus['GO_TO_GATE'], 1), (dairy_flat_airways.models.FlightStatus['BOARDED'], 2), (dairy_flat_airways.models.FlightStatus['IN_FLIGHT'], 3), (dairy_flat_airways.models.FlightStatus['COMPLETED'], 4), (dairy_flat_airways.models.FlightStatus['CANCELLED'], 5), (dairy_flat_airways.models.FlightStatus['DELAYED'], 6), (dairy_flat_airways.models.FlightStatus['DIVERTED'], 7), (dairy_flat_airways.models.FlightStatus['UNKNOWN'], 8)], default=dairy_flat_airways.models.FlightStatus['SCHEDULED'], max_length=30),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[(dairy_flat_airways.models.FlightStatus['SCHEDULED'], 0), (dairy_flat_airways.models.FlightStatus['GO_TO_GATE'], 1), (dairy_flat_airways.models.FlightStatus['BOARDED'], 2), (dairy_flat_airways.models.FlightStatus['IN_FLIGHT'], 3), (dairy_flat_airways.models.FlightStatus['COMPLETED'], 4), (dairy_flat_airways.models.FlightStatus['CANCELLED'], 5), (dairy_flat_airways.models.FlightStatus['DELAYED'], 6), (dairy_flat_airways.models.FlightStatus['DIVERTED'], 7), (dairy_flat_airways.models.FlightStatus['UNKNOWN'], 8)], default=dairy_flat_airways.models.TicketStatus['SCHEDULED'], max_length=30),
        ),
    ]
