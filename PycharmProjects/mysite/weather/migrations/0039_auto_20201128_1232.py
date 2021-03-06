# Generated by Django 3.1.3 on 2020-11-28 10:32

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0038_auto_20201128_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyreq',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 10, 32, 3, 802374, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='CityWeather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField(default=0)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 11, 28, 10, 32, 3, 801339, tzinfo=utc), verbose_name='date requested')),
                ('description', models.CharField(default='', max_length=200)),
                ('icon', models.CharField(default='', max_length=10)),
                ('cod', models.IntegerField(default=0)),
                ('city_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.city')),
            ],
        ),
    ]
