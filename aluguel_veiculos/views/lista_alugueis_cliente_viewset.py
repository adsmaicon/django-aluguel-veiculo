from rest_framework import generics
from aluguel_veiculos.models.aluguel import Aluguel
from aluguel_veiculos.serializers.lista_alugueis_cliente_serializer import ListaAlugueisClienteSerializer


class ListaAlugueisClienteViewset(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""

    def get_queryset(self):
        queryset = Aluguel.objects.filter(cliente_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaAlugueisClienteSerializer
