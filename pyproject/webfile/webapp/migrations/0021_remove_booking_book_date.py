# Generated by Django 5.0.1 on 2024-04-10 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0020_remove_booking_book_time_booking_book_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='book_date',
        ),
    ]
