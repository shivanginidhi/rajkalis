# Generated by Django 2.1 on 2018-08-18 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_song_is_favourite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mail_id', models.CharField(max_length=200)),
                ('phone_no', models.IntegerField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
