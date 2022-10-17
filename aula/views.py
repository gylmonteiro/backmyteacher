from rest_framework.views import Response, APIView
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404

from aula.serializers import CadastrarAulaSerializer, AulaSerializer
from aula.models import Aula
from teacher.models import Professor



class CadastrarAulaAPIView(APIView):
    def post(self, request, id, format=None):
        professor = get_object_or_404(Professor, id=id)
        serializer = CadastrarAulaSerializer(data=request.data)
        if serializer.is_valid():
            aula = Aula(**serializer.data, professor=professor)
            aula.save()
            aula_serializer = AulaSerializer(aula, many=False)
            return Response(aula_serializer.data, status=HTTP_201_CREATED)
        return Response({"message": "Houveram erros na validação", "erros": serializer.errors}, status=HTTP_400_BAD_REQUEST)
