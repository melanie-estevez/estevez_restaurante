from rest_framework import serializers
from restaurante.models import CategoriaMenu


class CategoriaMenuSerializer(serializers.ModelSerializer):

    def validate_nombre(self, value):
        value = value.strip()

        if len(value) < 3:
            raise serializers.ValidationError(
                'El nombre debe tener al menos 3 caracteres.'
            )

        queryset = CategoriaMenu.objects.filter(
            nombre__iexact=value
        )

        if self.instance:
            queryset = queryset.exclude(
                pk=self.instance.pk
            )

        if queryset.exists():
            raise serializers.ValidationError(
                'Ya existe una categoría con ese nombre.'
            )

        return value

    def validate_descripcion(self, value):
        return value.strip()

    class Meta:
        model = CategoriaMenu

        fields = [
            'id',
            'nombre',
            'descripcion',
        ]

        read_only_fields = [
            'id',
        ]