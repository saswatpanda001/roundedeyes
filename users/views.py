from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.models import UserContactData
from users.serializers import UserContactSerializer


class ListCreateContactAPIView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserContactSerializer
    queryset = UserContactData.objects.all()


class RetrieveUpdateDestroyConatactAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = UserContactData.objects.all()
    serializer_class = UserContactSerializer
