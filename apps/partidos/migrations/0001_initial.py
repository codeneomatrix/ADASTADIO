# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('torneo', models.CharField(max_length=45, blank=True)),
                ('visitante', models.CharField(max_length=30, blank=True)),
                ('fecha', models.DateField(null=True, blank=True)),
                ('hora', models.TimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
