# Generated by Django 5.1.7 on 2025-03-18 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('System_Monitor_Servers', '0002_alert_alertrule_cpumetric_datastorage_diskmetric_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoScaler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CloudIntegration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SecurityMonitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
