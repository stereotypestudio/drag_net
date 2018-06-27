# Generated by Django 2.0.6 on 2018-06-26 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('dateTime', models.DateTimeField()),
                ('desc', models.TextField()),
            ],
        ),
    ]
