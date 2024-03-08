from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from movies.models import Movie
from movies.serializer import MovieSerilizers


class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerilizers


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerilizers
