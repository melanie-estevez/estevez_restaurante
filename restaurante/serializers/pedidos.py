from rest_framework import serializers

from restaurante.models import Pedido


class PedidoSerializer(serializers.ModelSerializer):

    cliente_nombre = serializers.CharField(
        source='cliente.nombre_completo',
        read_only=True
    )

    class Meta:
        model = Pedido

        fields = [
            'id',
            'cliente',
            'cliente_nombre',
            'fecha_pedido',
            'estado',
            'total',
        ]

        read_only_fields = [
            'id',
            'fecha_pedido',
        ]