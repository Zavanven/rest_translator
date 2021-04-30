from django.shortcuts import render
from django.http import Http404
from django.utils import translation
from rest_framework import request, serializers, status
from rest_framework import response
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Translation
from .serializer import TranslationSerializer
from rest_framework.permissions import IsAuthenticated

class TranslationList(APIView):
    """
    Wyswietlanie wszystkich dostepnych translacji lub dodanie nowej
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        translations = Translation.objects.all()
        serializer = TranslationSerializer(translations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TranslationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TranslationDetail(APIView):
    """
    Wyswietlanie tlumaczenia, jego aktualizacja i usuniecie
    """
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Translation.objects.get(pk=pk)
        except Translation.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = TranslationSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        translation = self.get_object(pk)
        serializer = TranslationSerializer(translation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        translation = self.get_object(pk)
        translation.delete()
        return Response(status=status.status.HTTP_204_NO_CONTENT)