# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 15:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import ubigeo.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('nacionalidad_m', models.CharField(max_length=120)),
                ('nacionalidad_f', models.CharField(blank=True, max_length=120, null=True)),
                ('idioma', models.CharField(blank=True, max_length=120, null=True)),
                ('latitud', models.CharField(blank=True, max_length=50, null=True)),
                ('longitud', models.CharField(blank=True, max_length=50, null=True)),
                ('bandera', models.FileField(blank=True, max_length=150, null=True, upload_to=ubigeo.models.directorio_bandera, verbose_name='bandera')),
                ('escudo', models.FileField(blank=True, max_length=150, null=True, upload_to=ubigeo.models.directorio_bandera, verbose_name='escudo')),
                ('codigo_internacional', models.CharField(max_length=7)),
                ('codigo_pais', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'verbose_name_plural': 'Pais',
                'verbose_name': 'Pais',
                'permissions': (('list_pais', 'Can list pais'), ('get_pais', 'Can get pais'), ('list_paistipoubigeo', 'Can list paistipoubigeo'), ('get_paistipoubigeo', 'Can get paistipoubigeo')),
            },
        ),
        migrations.CreateModel(
            name='PaisTipoUbigeo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('orden', models.IntegerField(blank=True, null=True)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pais_pais', to='ubigeo.Pais')),
            ],
            options={
                'verbose_name_plural': 'pais tipo ubigeos',
                'verbose_name': 'pais tipo ubigeo',
                'permissions': (('list_paistipoubigeo', 'Can list paistipoubigeo'), ('get_paistipoubigeo', 'Can get paistipoubigeo')),
            },
        ),
        migrations.CreateModel(
            name='TipoUbigeo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('zoom', models.IntegerField(blank=True, null=True)),
                ('estado', models.CharField(default='1', max_length=1, verbose_name='Estado')),
            ],
            options={
                'verbose_name_plural': 'Tipo ubigeo',
                'verbose_name': 'Tipo ubigeo',
                'permissions': (('list_tipoubigeo', 'Can list tipoubigeo'), ('get_tipoubigeo', 'Can get tipoubigeo')),
            },
        ),
        migrations.CreateModel(
            name='Ubigeo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(blank=True, max_length=10, null=True)),
                ('capital', models.CharField(blank=True, max_length=20, null=True)),
                ('latitud', models.CharField(blank=True, max_length=100, null=True)),
                ('longitud', models.CharField(blank=True, max_length=100, null=True)),
                ('codigo_postal', models.CharField(blank=True, max_length=30, null=True)),
                ('codigo_area', models.CharField(blank=True, max_length=30, null=True)),
                ('estado', models.CharField(default='1', max_length=1, null=True, verbose_name='Estado')),
                ('foto', models.FileField(blank=True, max_length=120, null=True, upload_to=ubigeo.models.directorio_bandera, verbose_name='foto')),
                ('padre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hijos', to='ubigeo.Ubigeo')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ubigeo_pais', to='ubigeo.Pais')),
                ('tipo_ubigeo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ubigeo_tipo_ubigeo', to='ubigeo.TipoUbigeo')),
            ],
            options={
                'verbose_name_plural': 'Ubigeos',
                'verbose_name': 'Ubigeo',
                'permissions': (('list_ubigeo', 'Can list ubigeo'), ('get_ubigeo', 'Can get ubigeo')),
            },
        ),
        migrations.AddField(
            model_name='paistipoubigeo',
            name='tipo_ubigeo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pais_tipo_ubigeo', to='ubigeo.TipoUbigeo'),
        ),
        migrations.AddField(
            model_name='pais',
            name='pais_tipo_ubigeo',
            field=models.ManyToManyField(related_name='pais_tipo_ubigeo_set', through='ubigeo.PaisTipoUbigeo', to='ubigeo.TipoUbigeo', verbose_name='PaisTipoUbigeo'),
        ),
    ]
