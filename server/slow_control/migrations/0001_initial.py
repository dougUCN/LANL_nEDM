# Generated by Django 3.2.12 on 2022-05-10 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('states', models.TextField()),
                ('current_state', models.TextField()),
                ('is_online', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Runfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('q_order', models.PositiveIntegerField(default=0)),
                ('start_time', models.DateTimeField(null=True)),
                ('device_states', models.JSONField(null=True)),
                ('runtime', models.FloatField(default=0)),
                ('status', models.CharField(default='Queued', max_length=100)),
            ],
        ),
    ]
