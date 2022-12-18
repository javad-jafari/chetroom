from rest_framework import serializers
from django.contrib.auth import get_user_model
from chat.consumers import Message 


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields =  ["username", "last_login", "is_staff", "is_active"]



class MesssageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields =  ["user", "content", "timestamp" ]