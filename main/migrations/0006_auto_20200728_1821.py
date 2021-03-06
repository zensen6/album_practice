# Generated by Django 3.0.8 on 2020-07-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200728_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(null=True, upload_to='albums/'),
        ),
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.ImageField(null=True, upload_to='artists/'),
        ),
        migrations.AddField(
            model_name='song',
            name='song_src',
            field=models.FileField(null=True, upload_to='songs/'),
        ),
    ]
