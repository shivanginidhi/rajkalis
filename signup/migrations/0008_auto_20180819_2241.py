# Generated by Django 2.1 on 2018-08-19 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0007_auto_20180819_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSignup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_password', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=100)),
                ('aadhar', models.IntegerField(max_length=100)),
                ('photo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='UsersSignup',
        ),
    ]