# Generated by Django 2.0.6 on 2018-06-26 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
        ('events_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='queen',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='users_app.User'),
            preserve_default=False,
        ),
    ]
