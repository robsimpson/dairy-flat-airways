# Generated by Django 4.1 on 2023-06-09 09:47

import dairy_flat_airways.models
from django.db import migrations, models
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dairy_flat_airways', '0028_alter_flight_status_alter_ticket_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='legs',
            field=models.CharField(default='[]', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flight',
            name='status',
            field=enumfields.fields.EnumField(default='Scheduled', enum=dairy_flat_airways.models.FlightStatus, max_length=10),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=enumfields.fields.EnumField(default='Scheduled', enum=dairy_flat_airways.models.TicketStatus, max_length=10),
        ),
    ]