from rest_framework import serializers
from users.models import UserContactData

class UserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContactData
        fields = "__all__"
        