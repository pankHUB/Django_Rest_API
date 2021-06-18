from django.shortcuts import render
from  rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieModel

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieModel.objects.all()
    serializer_class = MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset=MovieModel.objects.filter(typ='action')
    serializer_class=MovieSerializer

class LS(viewsets.ModelViewSet):
    queryset=MovieModel.objects.filter(typ='ls')
    serializer_class=MovieSerializer