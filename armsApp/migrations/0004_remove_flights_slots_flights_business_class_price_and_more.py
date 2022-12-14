# Generated by Django 4.0.3 on 2022-04-27 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armsApp', '0003_flights'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flights',
            name='slots',
        ),
        migrations.AddField(
            model_name='flights',
            name='business_class_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='flights',
            name='business_class_slots',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='flights',
            name='economy_class_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='flights',
            name='economy_class_slots',
            field=models.IntegerField(default=0),
        ),
    ]
