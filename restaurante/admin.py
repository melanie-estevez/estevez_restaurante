from django.contrib import admin
from .models import Cliente
from .models import CategoriaMenu
from .models import Plato
from .models import Pedido
from .models import DetallePedido
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id','nombre_completo','telefono','correo','fecha_registro',]
    search_fields = ['nombre_completo','correo','telefono',]
    ordering = ['id']
    
@admin.register(CategoriaMenu)
class CategoriaMenuAdmin(admin.ModelAdmin):
    list_display = ['id','nombre']
    search_fields = ['nombre','descripcion']
    ordering = ['nombre']
    
@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    list_display = [ 'id','nombre','precio','disponible','categoria']
    list_filter = ['disponible','categoria']
    search_fields = ['nombre','descripcion']
    list_editable = ['precio','disponible']
    
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id','cliente','fecha_pedido','estado','total']
    list_filter = ['estado','fecha_pedido']
    search_fields = ['cliente__nombre_completo']
    list_editable = ['estado']
    ordering = ['-fecha_pedido']

@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ['id','pedido','plato','cantidad','precio_unitario','subtotal']
    list_filter = ['plato']
    search_fields = ['plato__nombre']
    ordering = ['id']