# Generated by Django 4.0.3 on 2022-07-03 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_room_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='Description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='room',
            name='adress',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='room',
            name='facilities',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='room',
            name='img',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='room',
            name='rating',
            field=models.FloatField(blank=True, default=8.9),
        ),
        migrations.AddField(
            model_name='room',
            name='review',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]