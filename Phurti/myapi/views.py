from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import categories
from .serializers import categoriesSerializer


# class categoriesList(APIView):
#     def get(self, request, *args, **kwargs):
#         categories1 = categories.objects.all()
#         serializer = categoriesSerializer(categories1, many=True)
#         return Response(serializer.data)

from rest_framework import viewsets

from .serializers import categoriesSerializer
from .models import categories


class categoriesViewSet(viewsets.ModelViewSet):
    queryset = categories.objects.all()
    serializer_class = categoriesSerializer