# Generated by Django 3.0.5 on 2020-04-07 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor', models.CharField(max_length=20)),
                ('moisture_value', models.CharField(max_length=3)),
                ('moisture', models.CharField(max_length=5)),
                ('temperature', models.CharField(max_length=5)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
