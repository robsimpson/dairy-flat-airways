# Generated by Django 4.1 on 2023-06-11 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dairy_flat_airways', '0032_ticket_owner_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='owner_email',
        ),
    ]
