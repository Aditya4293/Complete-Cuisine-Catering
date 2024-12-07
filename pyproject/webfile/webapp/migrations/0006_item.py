# Generated by Django 5.0.1 on 2024-04-01 06:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('i_id', models.AutoField(primary_key=True, serialize=False)),
                ('i_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='static/img/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.category')),
            ],
        ),
    ]