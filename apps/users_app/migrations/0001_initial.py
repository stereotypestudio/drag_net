# Generated by Django 2.0.6 on 2018-06-25 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dragName', models.CharField(max_length=255)),
                ('houseName', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password_hash', models.CharField(max_length=255)),
            ],
        ),
    ]