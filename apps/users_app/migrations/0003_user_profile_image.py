# Generated by Django 2.0.6 on 2018-06-27 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0002_user_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
