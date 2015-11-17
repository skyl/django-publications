# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0005_renameToKeywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]
