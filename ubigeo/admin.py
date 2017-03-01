from django.contrib import admin

# Register your models here.
from .models import Ubigeo

# Register your models here.


class UbigeoAdmin(admin.ModelAdmin):

    """docstring for UbigeoAdmin"""

    list_display = ("nombre", "codigo", "estado",
                    "pais", "tipo_ubigeo", "padre")
    search_fields = ("nombre", "codigo",)
    list_per_page = 7000


admin.site.register(Ubigeo, UbigeoAdmin)
