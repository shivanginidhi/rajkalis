# Generated by Django 2.1 on 2018-08-19 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_auto_20180819_2158'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='UserLogin',
        ),
    ]
