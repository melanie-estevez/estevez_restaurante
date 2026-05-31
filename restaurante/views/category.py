from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from restaurante.models import CategoriaMenu
from restaurante.serializers import CategoriaMenuSerializer
from restaurante.permissions import IsStaffOrReadOnly
from restaurante.filters import CategoriaMenuFilter


class CategoriaMenuViewSet(ModelViewSet):
    queryset = CategoriaMenu.objects.all()
    serializer_class = CategoriaMenuSerializer

    permission_classes = [IsStaffOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_class = CategoriaMenuFilter

    search_fields = [
        'nombre',
        'descripcion',
    ]

    ordering_fields = [
        'id',
        'nombre',
    ]

    ordering = ['nombre']