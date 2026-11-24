from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import ObraArte
from .serializers import ObraArteSerializer


class ListarCriarObras(generics.ListCreateAPIView):

    queryset = ObraArte.objects.all()
    serializer_class = ObraArteSerializer

class GerenciarObra(generics.RetrieveUpdateDestroyAPIView):

    queryset = ObraArte.objects.all()
    serializer_class = ObraArteSerializer

@api_view(['GET'])
def obras_por_artista(request, nome):

    obras = ObraArte.objects.filter(
        artista__icontains=nome
    )

    serializer = ObraArteSerializer(obras, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def obras_por_movimento(request, nome):

    obras = ObraArte.objects.filter(
        movimento_artistico__icontains=nome
    )

    serializer = ObraArteSerializer(obras, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def obras_por_museu(request, nome):

    obras = ObraArte.objects.filter(
        museu__icontains=nome
    )

    serializer = ObraArteSerializer(obras, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def obras_por_ano(request, ano):

    obras = ObraArte.objects.filter(
        ano_criacao=ano
    )

    serializer = ObraArteSerializer(obras, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def buscar_obra(request):

    nome = request.query_params.get('nome', '')

    if not nome:
        return Response(
            {'erro': 'Informe o nome da obra.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    obras = ObraArte.objects.filter(
        nome__icontains=nome
    )

    serializer = ObraArteSerializer(obras, many=True)

    return Response(serializer.data)