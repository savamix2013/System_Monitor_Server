# Generated by Django 5.1.7 on 2025-03-18 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('System_Monitor_Servers', '0004_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default='2025-01-01T00:00:00'),
            preserve_default=False,
        ),
    ]
