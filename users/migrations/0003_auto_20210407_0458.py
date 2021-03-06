# Generated by Django 3.0.4 on 2021-04-07 04:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/users/formal1.jpeg', upload_to='media/users'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
