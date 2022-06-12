from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from movies.models import Movies
from movies.serializers import MovieSerializer


class ListCreateMoviesAPIView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = MovieSerializer
    queryset = Movies.objects.all()


class RetrieveUpdateDestroyMoviesAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
