import django_filters
from restaurante.models import CategoriaMenu, Cliente, Plato, Pedido, DetallePedido

class CategoriaMenuFilter(django_filters.FilterSet):

    nombre = django_filters.CharFilter(
        lookup_expr='icontains'
    )

    class Meta:
        model = CategoriaMenu
        fields = ['nombre']


class ClienteFilter(django_filters.FilterSet):

    nombre_completo = django_filters.CharFilter(
        lookup_expr='icontains'
    )

    correo = django_filters.CharFilter(
        lookup_expr='icontains'
    )

    fecha_registro = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Cliente
        fields = [
            'nombre_completo',
            'correo',
            'fecha_registro',
        ]
        

class PlatoFilter(django_filters.FilterSet):

    nombre = django_filters.CharFilter(
        lookup_expr='icontains'
    )

    disponible = django_filters.BooleanFilter()

    categoria = django_filters.NumberFilter()

    precio_min = django_filters.NumberFilter(
        field_name='precio',
        lookup_expr='gte'
    )

    precio_max = django_filters.NumberFilter(
        field_name='precio',
        lookup_expr='lte'
    )

    class Meta:
        model = Plato
        fields = [
            'nombre',
            'disponible',
            'categoria',
        ]


class PedidoFilter(django_filters.FilterSet):

    cliente = django_filters.NumberFilter()

    estado = django_filters.CharFilter(
        lookup_expr='iexact'
    )

    total_min = django_filters.NumberFilter(
        field_name='total',
        lookup_expr='gte'
    )

    total_max = django_filters.NumberFilter(
        field_name='total',
        lookup_expr='lte'
    )

    class Meta:
        model = Pedido
        fields = [
            'cliente',
            'estado',
        ]

class DetallePedidoFilter(django_filters.FilterSet):

    pedido = django_filters.NumberFilter()

    plato = django_filters.NumberFilter()

    cantidad_min = django_filters.NumberFilter(
        field_name='cantidad',
        lookup_expr='gte'
    )

    cantidad_max = django_filters.NumberFilter(
        field_name='cantidad',
        lookup_expr='lte'
    )

    class Meta:
        model = DetallePedido
        fields = [
            'pedido',
            'plato',
        ]