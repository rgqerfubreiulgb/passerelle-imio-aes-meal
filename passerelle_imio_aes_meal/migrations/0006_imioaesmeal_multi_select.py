# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-29 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passerelle_imio_aes_meal', '0005_imioaesmeal_personal_labels'),
    ]

    operations = [
        migrations.AddField(
            model_name='imioaesmeal',
            name='multi_select',
            field=models.BooleanField(default=True, verbose_name='Allows to select multiple items'),
        ),
    ]
