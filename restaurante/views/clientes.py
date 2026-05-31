from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from restaurante.models import Cliente
from restaurante.serializers import ClienteSerializer
from restaurante.permissions import IsStaffOrReadOnly


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all().order_by('id')
    serializer_class = ClienteSerializer

    permission_classes = [IsStaffOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    search_fields = [
        'nombre_completo',
        'correo',
        'telefono',
    ]

    filterset_fields = [
        'correo',
    ]

    ordering_fields = [
        'nombre_completo',
        'fecha_registro',
        'id',
    ]