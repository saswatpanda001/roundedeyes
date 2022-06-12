from quiz.serializers import QuizSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from quiz.models import Quiz
from quiz.serializers import QuizSerializer


class ListCreateQuizAPIView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    


class RetrieveUpdateDestroyQuizAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    