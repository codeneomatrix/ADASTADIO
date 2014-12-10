# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20, blank=True)),
                ('precio', models.IntegerField(null=True, blank=True)),
                ('asientosdisponibles', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20, blank=True)),
                ('cantidaboletos', models.IntegerField(null=True, blank=True)),
                ('tratoespecial', models.CharField(max_length=20, blank=True)),
                ('puertasacceso', models.CharField(max_length=20, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='areas',
            name='idzona',
            field=models.ForeignKey(to='controlzonas.Zona'),
            preserve_default=True,
        ),
    ]
