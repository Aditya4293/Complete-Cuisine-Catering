# Generated by Django 5.0.1 on 2024-04-10 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_alter_package_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='no_of_person',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
