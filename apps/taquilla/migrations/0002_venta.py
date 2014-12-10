# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
        ('partidos', '0001_initial'),
        ('controlzonas', '0001_initial'),
        ('taquilla', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(null=True, blank=True)),
                ('tarjeta', models.CharField(default=0, max_length=16)),
                ('tipoventa', models.CharField(max_length=30, blank=True)),
                ('numeroasiento', models.IntegerField(default=0)),
                ('monto', models.IntegerField(null=True, blank=True)),
                ('area', models.ForeignKey(to='controlzonas.Areas')),
                ('descuentoa', models.ForeignKey(to='taquilla.Descuento')),
                ('nickuser', models.ForeignKey(to='inicio.Perfiles')),
                ('partido', models.ForeignKey(to='partidos.Partido')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
