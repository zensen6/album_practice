# Generated by Django 3.0.8 on 2020-07-28 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.DurationField(),
        ),
    ]
