from django.http import Http404
from rest_framework import request, serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Language
from .serializers import LanguageSerializer
from rest_framework.permissions import IsAuthenticated

class LanguageList(APIView):
    """
    Wyswietlanie wszystkich dostepnych jezykow na sklepach lub dodanie nowego
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LanguageDetail(APIView):
    """
    Wyswietlanie jezyka, aktualizacja jego danych lub jego usuniecie
    """
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Language.objects.get(pk=pk)
        except Language.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        language = self.get_object(pk)
        serializer = LanguageSerializer(language)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        language = self.get_object(pk)
        serializer = LanguageSerializer(language, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        language = self.get_object(pk)
        language.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)