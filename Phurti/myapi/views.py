from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import categories
from .serializers import categoriesSerializer

class categorieslist(APIView):
    def get(self, request):
        categories1 = categories.objects.all()
        serializer = categoriesSerializer(categories1, many=True)
        return Response(serializer.data)
