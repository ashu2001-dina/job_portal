# Generated by Django 3.0.6 on 2021-08-31 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210831_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, upload_to='media/resume_users/'),
        ),
    ]
