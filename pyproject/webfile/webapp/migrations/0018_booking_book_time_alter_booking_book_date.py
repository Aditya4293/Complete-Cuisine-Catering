# Generated by Django 5.0.1 on 2024-04-10 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_remove_booking_no_of_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='book_time',
            field=models.TimeField(default=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='book_date',
            field=models.DateField(),
        ),
    ]
