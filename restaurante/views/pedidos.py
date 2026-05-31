from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from decimal import Decimal

from restaurante.models import (
    Pedido,
    Cliente,
    Plato,
    DetallePedido
)

from restaurante.serializers import PedidoSerializer
from restaurante.permissions import IsStaffOrReadOnly
from restaurante.filters import PedidoFilter


class PedidoViewSet(ModelViewSet):

    queryset = Pedido.objects.select_related(
        'cliente'
    ).all()

    serializer_class = PedidoSerializer

    permission_classes = [
        IsStaffOrReadOnly
    ]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_class = PedidoFilter

    search_fields = [
        'cliente__nombre_completo',
        'estado',
    ]

    ordering_fields = [
        'id',
        'fecha_pedido',
        'total',
    ]

    ordering = [
        '-fecha_pedido'
    ]

    
    @action(detail=False, methods=['post'], url_path='crear-completo')
    def crear_completo(self, request):

        cliente_id = request.data.get('cliente')
        items = request.data.get('items', [])


        try:
            cliente = Cliente.objects.get(pk=cliente_id)
        except Cliente.DoesNotExist:
            return Response(
                {'error': 'Cliente no existe'},
                status=status.HTTP_404_NOT_FOUND
            )

        pedido = Pedido.objects.create(
            cliente=cliente,
            estado='PENDIENTE',
            total=0
        )

        total = Decimal('0.00')


        for item in items:

            try:
                plato = Plato.objects.get(pk=item['plato'])
            except Plato.DoesNotExist:
                pedido.delete()
                return Response(
                    {'error': f"Plato {item['plato']} no existe"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            cantidad = item['cantidad']
            subtotal = plato.precio * cantidad

            DetallePedido.objects.create(
                pedido=pedido,
                plato=plato,
                cantidad=cantidad,
                precio_unitario=plato.precio,
                subtotal=subtotal
            )

            total += subtotal

        pedido.total = total
        pedido.save()

        return Response(
            PedidoSerializer(pedido).data,
            status=status.HTTP_201_CREATED
        )