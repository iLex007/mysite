# Generated by Django 3.1.3 on 2020-11-13 13:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0010_auto_20201112_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 13, 13, 25, 17, 856415, tzinfo=utc), verbose_name='date requested'),
        ),
    ]