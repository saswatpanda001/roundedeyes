from django.urls import path, include
from quiz.views import ListCreateQuizAPIView,RetrieveUpdateDestroyQuizAPIView

app_name = "quiz"


urlpatterns = [
    path("", ListCreateQuizAPIView.as_view(),name="quiz_list"),
    path("<int:pk>", RetrieveUpdateDestroyQuizAPIView.as_view(),name="quiz_dt")
]
