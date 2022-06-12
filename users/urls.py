from django.urls import path, include
from users.views import ListCreateContactAPIView, RetrieveUpdateDestroyConatactAPIView

app_name = "contacts"


urlpatterns = [
    path("", ListCreateContactAPIView.as_view()),
    path("<int:pk>", RetrieveUpdateDestroyConatactAPIView.as_view())
]
