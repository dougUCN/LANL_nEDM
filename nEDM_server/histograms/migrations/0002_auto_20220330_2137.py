# Generated by Django 3.2.12 on 2022-03-30 21:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('histograms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='histogram',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='histogram',
            name='type',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]
