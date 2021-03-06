# Generated by Django 3.0.4 on 2021-04-07 04:58

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0005_auto_20210406_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='employee',
            field=models.ManyToManyField(blank=True, default=None, related_name='job_employee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=ckeditor.fields.RichTextField(default=None),
        ),
    ]
