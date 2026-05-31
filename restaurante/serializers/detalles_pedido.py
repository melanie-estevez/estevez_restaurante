from rest_framework import serializers

from restaurante.models import DetallePedido


class DetallePedidoSerializer(serializers.ModelSerializer):

    plato_nombre = serializers.CharField(
        source='plato.nombre',
        read_only=True
    )

    def validate_cantidad(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                'La cantidad debe ser mayor que cero.'
            )

        return value

    def validate_precio_unitario(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                'El precio unitario debe ser mayor que cero.'
            )

        return value

    class Meta:
        model = DetallePedido

        fields = [
            'id',
            'pedido',
            'plato',
            'plato_nombre',
            'cantidad',
            'precio_unitario',
            'subtotal',
        ]

        read_only_fields = [
            'id',
        ]