import logging

from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce

from ..models import Ubigeo

from backend_utils.logs import log_params
from backend_utils.permissions import ModelPermission
from backend_utils.pagination import ModelPagination

#from rest_framework import permissions
# from django.utils.translation import ugettext as _  # , ungettext

log = logging.getLogger(__name__)


class DynamicSerializerModel(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        super(DynamicSerializerModel, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class UbigeoSerializer(serializers.ModelSerializer):

    pais_nombre = serializers.SerializerMethodField()
    tipo_ubigeo_nombre = serializers.SerializerMethodField()
    padre_nombre = serializers.SerializerMethodField()
    # tipo_ubigeo_nombre = serializers.CharField(
    #    source='tipo_ubigeo.nombre')
    # padre_nombre = serializers.CharField(
    #    source='padre.nombre')

    # unidad_medida = UnidadMedidaSerializer(
    #    required=False, many=False, read_only=True)

    class Meta:
        model = Ubigeo
        fields = ("id", "nombre", "codigo", "estado",
                  "pais", "tipo_ubigeo", "padre",
                  "pais_nombre",
                  "tipo_ubigeo_nombre", "padre_nombre"
                  )  # '__all__'  # ('nombre',)
        # depth = 1

    def get_pais_nombre(self, obj):
        try:
            return obj.pais.nombre
        except:
            return 'sin pais'

    def get_tipo_ubigeo_nombre(self, obj):
        try:
            return obj.tipo_ubigeo.nombre
        except:
            return 'sin tipo_ubigeo'

    def get_padre_nombre(self, obj):
        try:
            return obj.padre.nombre
        except:
            return 'sin padre'

from oauth2_provider.ext.rest_framework import TokenHasScope
#from rest_framework.permissions import IsAuthenticated

from rest_framework.permissions import IsAuthenticated

# ModelPagination,
from rest_framework import pagination


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 10000


class UbigeoViewSet(viewsets.ModelViewSet):
    queryset = Ubigeo.objects.filter(id__isnull=False)
    serializer_class = UbigeoSerializer
    # paginate_by = 8
    pagination_class = StandardResultsSetPagination
    #permission_classes = [ModelPermission, TokenHasScope]
    # required_scopes = ['ubigeo', ]  # , 'write' , TokenHasScope
