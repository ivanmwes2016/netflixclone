from django.shortcuts import render
from django.http import JsonResponse
from BankendAPI.models import Movie
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer
from rest_framework.parsers import JSONParser


# MovieList
@api_view(['GET'])
def moviesList(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


# Movie Detail
@api_view(['GET'])
def movieDatail(request, pk):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=False)
    return Response(serializer.data)

# Create Movie
@api_view(['POST'])
def insertMovie(request):
    data = JSONParser.parse(request)
    serializer = MovieSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
