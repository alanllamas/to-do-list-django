# Generated by Django 2.0.5 on 2018-10-05 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20181005_0508'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='time_remaining',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True),
        ),
    ]
