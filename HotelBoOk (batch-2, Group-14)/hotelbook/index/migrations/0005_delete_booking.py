# Generated by Django 2.2.6 on 2019-11-07 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_hotels_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]