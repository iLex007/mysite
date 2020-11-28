# Generated by Django 3.1.3 on 2020-11-28 09:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0033_auto_20201127_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='id',
        ),
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cityweather',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 9, 33, 22, 151680, tzinfo=utc), verbose_name='date requested'),
        ),
        migrations.AlterField(
            model_name='historyreq',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 9, 33, 22, 152677, tzinfo=utc)),
        ),
    ]