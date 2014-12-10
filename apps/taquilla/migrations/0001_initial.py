# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grupo', models.CharField(max_length=30, blank=True)),
                ('descuento', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
