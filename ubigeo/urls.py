from django.conf.urls import url, include
from rest_framework import routers

from .views.ubigeo_view import UbigeoViewSet

router = routers.DefaultRouter()

router.register(r'ubigeos', UbigeoViewSet)

urlpatterns = [

    url(r'^', include(router.urls)),

]
