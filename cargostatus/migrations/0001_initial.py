# Generated by Django 2.2.1 on 2019-05-06 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargostatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=30)),
                ('who_maked', models.CharField(blank=True, max_length=20)),
                ('data_time', models.DateTimeField(auto_now=True)),
                ('delta', models.CharField(blank=True, max_length=30)),
                ('customer_rate', models.CharField(blank=True, max_length=30)),
                ('rate_carriage', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
