# Generated by Django 3.0.5 on 2020-06-10 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logger', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=50)),
                ('trace', models.TextField()),
                ('msg', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('state', models.BooleanField()),
                ('value', models.CharField(blank=True, max_length=10, null=True)),
                ('state_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='state_name', to='data.Object')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('temperature', models.CharField(blank=True, max_length=5, null=True)),
                ('humidity', models.CharField(blank=True, max_length=5, null=True)),
                ('moisture', models.CharField(blank=True, max_length=5, null=True)),
                ('sensor_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sensor_name', to='data.Object')),
            ],
        ),
    ]
