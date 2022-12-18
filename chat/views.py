from django.shortcuts import render
from chat.models import Room
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

# def index_view(request):
#     from rest_framework import serializers

#     class ser(serializers.Serializer):
#         id = serializers.IntegerField()
#         name = serializers.CharField()

    
#     data = {'rooms': ser(Room.objects.all().values("name","id"), many=True).data}
#     print(data)
#     return JsonResponse(data)

def index_view(request):
    return render(request, 'index.html', {
        'rooms': Room.objects.all(),
    })



def room_view(request, room_name):
    chat_room = get_object_or_404(Room, name=room_name)
    return render(request, 'room.html', {
        'room': chat_room,
    })
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import  get_user_model
from rest_framework.exceptions import ValidationError
class Login(APIView):
    def post(self, request, format=None):
        username = request.data.get("username", None)
        if username is None:
            raise ValidationError("username is requierd !")
        user = get_user_model().objects.get(username=username)
        if user is not None:
            login(request, user)
            return Response({"login":"ok"}, status=200)
        else:
            return Response({"login":"failed"}, status=400)

class Logout(APIView):
    def get(self, request, format=None):
        try:
            logout(request)
            return Response({"logout":"ok"}, status=200)
        except:
            return Response({"logout":"fail"}, status=400)









