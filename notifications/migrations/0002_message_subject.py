# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='subject',
            field=models.CharField(help_text='Subject header for emails ', max_length=100, null=True),
        ),
    ]
