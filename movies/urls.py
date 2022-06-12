from django.urls import path, include
from movies.views import ListCreateMoviesAPIView, RetrieveUpdateDestroyMoviesAPIView
app_name = "movies"


urlpatterns = [
    path("", ListCreateMoviesAPIView.as_view()),
    path("<int:pk>",RetrieveUpdateDestroyMoviesAPIView.as_view())
]
