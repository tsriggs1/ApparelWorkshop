# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-18 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_product_editorial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='editorial',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
