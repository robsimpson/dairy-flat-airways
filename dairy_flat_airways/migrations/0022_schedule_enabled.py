# Generated by Django 4.1 on 2023-06-05 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairy_flat_airways', '0021_flight_status_ticket_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
