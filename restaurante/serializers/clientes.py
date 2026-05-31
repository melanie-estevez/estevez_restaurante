from rest_framework import serializers
from restaurante.models.clientes import Cliente


class ClienteSerializer(serializers.ModelSerializer):

    def validate_nombre_completo(self, value):
        value = value.strip()

        if len(value) < 3:
            raise serializers.ValidationError(
                "El nombre debe tener al menos 3 caracteres."
            )

        return value

    def validate_telefono(self, value):
        value = value.strip()

        if len(value) < 7:
            raise serializers.ValidationError(
                "El teléfono debe tener al menos 7 caracteres."
            )

        return value

    def validate_correo(self, value):
        correo = value.lower()

        queryset = Cliente.objects.filter(correo=correo)

        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(
                "Este correo ya está registrado."
            )

        return correo

    class Meta:
        model = Cliente
        fields = [
            'id',
            'nombre_completo',
            'telefono',
            'correo',
            'fecha_registro',
        ]

        read_only_fields = [
            'id',
            'fecha_registro',
        ]