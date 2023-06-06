# Generated by Django 4.1 on 2023-05-30 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dairy_flat_airways', '0014_flight_id_alter_flight_flight_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='flight',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='dairy_flat_airways.flight'),
            preserve_default=False,
        ),
    ]
