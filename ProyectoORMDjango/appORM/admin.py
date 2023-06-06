from django.contrib import admin
from appORM.models import *

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
