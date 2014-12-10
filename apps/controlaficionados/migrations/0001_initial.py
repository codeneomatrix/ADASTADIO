# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controlpersonal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='perfilesafi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, blank=True)),
                ('telefono', models.CharField(max_length=15, blank=True)),
                ('direccion', models.CharField(max_length=50, blank=True)),
                ('fecharegistro', models.DateField(null=True, blank=True)),
                ('idcoordinador', models.ForeignKey(to='controlpersonal.perfilesper')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
