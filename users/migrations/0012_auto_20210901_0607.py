# Generated by Django 3.0.6 on 2021-09-01 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20210901_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, upload_to='media/resume_users/'),
        ),
    ]
