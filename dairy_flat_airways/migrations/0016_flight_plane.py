# Generated by Django 4.1 on 2023-05-30 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dairy_flat_airways', '0015_ticket_flight'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='plane',
            field=models.ForeignKey(default='DF1', on_delete=django.db.models.deletion.PROTECT, to='dairy_flat_airways.plane'),
            preserve_default=False,
        ),
    ]
