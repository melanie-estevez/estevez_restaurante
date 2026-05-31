from rest_framework import serializers

from restaurante.models import Plato


class PlatoSerializer(serializers.ModelSerializer):

    categoria_nombre = serializers.CharField(
        source='categoria.nombre',
        read_only=True
    )

    def validate_nombre(self, value):
        value = value.strip()

        if len(value) < 2:
            raise serializers.ValidationError(
                'El nombre debe tener al menos 2 caracteres.'
            )

        return value

    def validate_precio(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                'El precio debe ser mayor que cero.'
            )

        return value

    def validate_descripcion(self, value):
        return value.strip()

    class Meta:
        model = Plato

        fields = [
            'id',
            'categoria',
            'categoria_nombre',
            'nombre',
            'descripcion',
            'precio',
            'disponible',
        ]

        read_only_fields = [
            'id',
            'categoria_nombre',
        ]