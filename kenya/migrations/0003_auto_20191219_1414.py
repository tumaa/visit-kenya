# Generated by Django 3.0 on 2019-12-19 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kenya', '0002_destination_destinationgallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='latitude',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='destination',
            name='longitute',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=6),
        ),
    ]
