# Generated by Django 5.0.1 on 2024-04-08 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_package1_remove_package_items_alter_package_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]