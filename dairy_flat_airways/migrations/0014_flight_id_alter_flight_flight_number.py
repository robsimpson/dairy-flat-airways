# Generated by Django 4.1 on 2023-05-30 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairy_flat_airways', '0013_remove_ticket_flight'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flight',
            name='flight_number',
            field=models.CharField(max_length=30),
        ),
    ]
