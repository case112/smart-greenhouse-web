# Generated by Django 3.0.5 on 2020-04-06 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dht22',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor', models.CharField(max_length=20)),
                ('temperature', models.CharField(max_length=5)),
                ('humidity', models.CharField(max_length=5)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
