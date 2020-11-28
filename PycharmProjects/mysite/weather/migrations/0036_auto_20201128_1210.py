# Generated by Django 3.1.3 on 2020-11-28 10:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0035_auto_20201128_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cityweather',
            name='city_name',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='cityweather',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 10, 10, 0, 96906, tzinfo=utc), verbose_name='date requested'),
        ),
        migrations.AlterField(
            model_name='historyreq',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 10, 10, 0, 150818, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]