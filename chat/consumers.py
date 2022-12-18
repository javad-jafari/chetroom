import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Room, Message
from .serializers import MesssageSerializer


class PublicGroupConsumer(WebsocketConsumer):


    def get_current_user(self):
        return self.scope["user"]

    def _check_user(self):
        return self.scope["user"].is_authenticated

    def chat_message(self, data):

        async_to_sync(self.channel_layer.group_send)(
            "echo",
            {
                "type": "chat.message",
                "text": data['message'],
                "user": self.scope["user"].username if self.scope["user"].is_authenticated else None
            },
        )
    
    def chat_is_typing(self, data):

        async_to_sync(self.channel_layer.group_send)(
            "echo",
            {
                "type": data['type'],
                "user": self.scope["user"].username if self.scope["user"].is_authenticated else None
            },
        )
    
    def get_old_message(self):
        msgs = Message.objects.filter(room=self.channel_name)
        return MesssageSerializer().data

    def chat_old_msg(self):
        print(self.channel_name)
        async_to_sync(self.channel_layer.send)(
                self.channel_name,
                {
                    "type": "chat.old.msg",
                    "text": "111111111111111111"
                },
            )
    
    def chat_user_joined(self):
        async_to_sync(self.channel_layer.group_send)(
                "echo",
                {
                    "type" : "chat.user.joined",
                    "text":self.scope["user"].username
                }
            )

    def chat_user_left(self):
        async_to_sync(self.channel_layer.group_send)(
                "echo",
                {
                    "type" : "chat.user.left",
                    "text":self.scope["user"].username
                }
            )
    
    def chat_online_users(self):
        async_to_sync(self.channel_layer.group_send)(
                "echo",
                {
                    "type" : "chat.online.users",
                    "text":Room.objects.get(name="echo").get_online_users()
                }
            )
    
    def add_to_group(self):
        async_to_sync(self.channel_layer.group_add)(
                "echo",
                self.channel_name
            )
        obj,_=Room.objects.get_or_create(name='echo')
        obj.join(self.get_current_user())

    def discard_from_group(self):
        async_to_sync(self.channel_layer.group_discard)(
                "echo",
                self.channel_name
            )


    command = {
        "chat_message":chat_message, 
        "chat_is_typing":chat_is_typing,
        "chat_old_msg":chat_old_msg,
        "chat_user_joined":chat_user_joined,
        "chat_user_left":chat_user_left,
        "chat_online_users":chat_online_users,
        "add_to_group":add_to_group,
        "discard_from_group":discard_from_group,
        }

    def connect(self):
        self.accept()

        if self._check_user():

            self.command["add_to_group"](self)
            self.command["chat_old_msg"](self)
            self.command["chat_user_joined"](self)
            self.command["chat_online_users"](self)

        else:
            self.disconnect()
    
    
    def disconnect(self, code):
        if self._check_user():
            self.command["chat_user_left"](self)
            self.command["discard_from_group"](self)

        obj=Room.objects.get(name='echo')
        obj.leave(self.get_current_user())
        return super().disconnect(code)
    
    def receive(self, text_data=None, bytes_data=None):

        text_data_j = json.loads(text_data)
        req_type = text_data_j["type"]

        self.command[req_type](self,text_data_j)


    
    def chat_message(self, event):
        forward_msg = {"msg":event["text"] ,'user':event["user"]}
        self.messages.append(forward_msg)

        self.send(text_data=json.dumps(
            {
                'user':event["user"], 
                'msg':event["text"], 
                'type':event["type"]
                }))
    
    def chat_is_typing(self, event):

        self.send(text_data=json.dumps(
            {
                'user':event["user"], 
                'type':event["type"]
                }))


    def chat_old_msg(self, event):

        self.send(
            text_data=json.dumps(
                {
                    "type": "chat_old_msg", 
                    "messages":event["text"]
                    }))

    def chat_user_joined(self, event):

        self.send(
            text_data=json.dumps(
                {
                    "type":"chat_user_joied",
                    "user":event["text"]
                }
            )
        )
    
    def chat_user_left(self,event):

        self.send(
            text_data=json.dumps(
                {
                    "type":"chat_user_left",
                    "user":event["text"]
                }
            )
        )
    def chat_online_users(self,event):

        self.send(
            text_data=json.dumps(
                {
                    "type":"chat_online_users",
                    "users":event["text"]
                }
            )
        )