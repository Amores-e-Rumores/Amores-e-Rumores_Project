# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 15:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amoreserumores_app', '0002_auto_20170209_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='cor',
            new_name='color',
        ),
    ]
