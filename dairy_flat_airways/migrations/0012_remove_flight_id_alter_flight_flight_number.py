# Generated by Django 4.1 on 2023-05-30 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairy_flat_airways', '0011_flight_id_alter_flight_flight_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='id',
        ),
        migrations.AlterField(
            model_name='flight',
            name='flight_number',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
