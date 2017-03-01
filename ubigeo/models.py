from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst, get_text_list
from uuid import uuid4
import os
from datetime import datetime, timedelta
from django.conf import settings

# Create your models here.


def directorio_bandera(self, filename):
    name, ext = filename, os.path.splitext(filename)[1]
    return os.path.join('backend/pais/', '{0}{1}{2}'.format(self.codigo_pais, '_b', ext
                                                            ))


class TipoUbigeo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(unique=True, max_length=100,
                              blank=False, null=False)
    zoom = models.IntegerField(blank=True, null=True)
    estado = models.CharField(
        capfirst(_('estado')), default='1', max_length=1,
        blank=False, null=False)

    class Meta:
        verbose_name = capfirst(_('Tipo ubigeo'))
        verbose_name_plural = capfirst(_('Tipo ubigeo'))
        permissions = (
            ('list_tipoubigeo', 'Can list tipoubigeo'),
            ('get_tipoubigeo', 'Can get tipoubigeo'),
        )

    def __str__(self):
        return self.nombre


class PaisTipoUbigeo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    pais = models.ForeignKey(
        'Pais', related_name='pais_pais', blank=False, null=False,
        on_delete=models.PROTECT)
    tipo_ubigeo = models.ForeignKey(
        'TipoUbigeo', related_name='pais_tipo_ubigeo',
        blank=False, null=False, on_delete=models.PROTECT)
    orden = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = _('pais tipo ubigeo')
        verbose_name_plural = _('pais tipo ubigeos')
        permissions = (
            ('list_paistipoubigeo', 'Can list paistipoubigeo'),
            ('get_paistipoubigeo', 'Can get paistipoubigeo'),
        )

    def __str__(self):
        return self.pais.nombre


class Pais(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(unique=True, max_length=100,
                              blank=False, null=False)
    nacionalidad_m = models.CharField(max_length=120, blank=False, null=False)
    nacionalidad_f = models.CharField(max_length=120, blank=True, null=True)
    idioma = models.CharField(max_length=120, blank=True, null=True)
    latitud = models.CharField(max_length=50, blank=True, null=True)
    longitud = models.CharField(max_length=50, blank=True, null=True)
    bandera = models.FileField(
        _('bandera'), upload_to=directorio_bandera,

        max_length=150, null=True, blank=True)
    escudo = models.FileField(
        _('escudo'), upload_to=directorio_bandera,

        max_length=150, null=True, blank=True)
    # Cambiar a False
    codigo_internacional = models.CharField(
        max_length=7, blank=False, null=False)
    codigo_pais = models.CharField(
        max_length=2, blank=True, null=True)
    pais_tipo_ubigeo = models.ManyToManyField(
        'TipoUbigeo', related_name='pais_tipo_ubigeo_set',
        verbose_name=_('PaisTipoUbigeo'), through='PaisTipoUbigeo')

    class Meta:
        verbose_name = capfirst(_('Pais'))
        verbose_name_plural = capfirst(_('Pais'))
        permissions = (
            ('list_pais', 'Can list pais'),
            ('get_pais', 'Can get pais'),
            ('list_paistipoubigeo', 'Can list paistipoubigeo'),
            ('get_paistipoubigeo', 'Can get paistipoubigeo'),
        )

    def __str__(self):
        return self.nombre


class Ubigeo(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, null=True, blank=True)
    capital = models.CharField(max_length=20, blank=True, null=True)
    latitud = models.CharField(max_length=100, blank=True, null=True)
    longitud = models.CharField(max_length=100, blank=True, null=True)
    codigo_postal = models.CharField(max_length=30, blank=True, null=True)
    codigo_area = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(
        capfirst(_('estado')), default='1', max_length=1,
        blank=False, null=True)
    padre = models.ForeignKey(
        'self', related_name="hijos", blank=True, null=True
    )
    foto = models.FileField(
        _('foto'), upload_to=directorio_bandera,

        max_length=120, null=True, blank=True)
    pais = models.ForeignKey(
        'Pais', related_name='ubigeo_pais', blank=False, null=False,
        on_delete=models.PROTECT)
    tipo_ubigeo = models.ForeignKey(
        'TipoUbigeo', related_name='ubigeo_tipo_ubigeo',
        blank=False, null=False, on_delete=models.PROTECT)

    class Meta:
        verbose_name = capfirst(_('ubigeo'))
        verbose_name_plural = capfirst(_('ubigeos'))
        permissions = (
            ('list_ubigeo', 'Can list ubigeo'),
            ('get_ubigeo', 'Can get ubigeo'),
        )

    def __str__(self):
        return self.nombre
