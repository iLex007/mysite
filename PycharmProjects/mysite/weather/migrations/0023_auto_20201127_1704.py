# Generated by Django 3.1.3 on 2020-11-27 15:04

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0022_auto_20201127_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='cityweather',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 15, 4, 45, 921798, tzinfo=utc), verbose_name='date requested'),
        ),
        migrations.AlterField(
            model_name='historyreq',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 15, 4, 45, 921798, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cityweather',
            name='city_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.city'),
        ),
    ]
