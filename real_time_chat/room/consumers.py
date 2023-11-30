import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Message, Room, users_all
from django.contrib.auth.models import User

#global variable
user_name=''

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        user = self.scope["user"]

        if user.is_authenticated:
            # global user_name
            user_name = str(user.username)
        
        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name
        )
        
        await self.accept()
        print("Connected to Chat Room: ", self.room_name)
        global users_all
        if user not in users_all:
            users_all[user_name] = str(self.room_name)
        print("USERS ENTERED ROOM: ", users_all)
        
    async def disconnect(self, close_code):
        user = str(self.scope["user"])
        await self.channel_layer.group_discard(
            self.room_group_name, 
            self.channel_name
            
        )
        print("DISCONNECT USER: ", user)
        global users_all
        users_all.pop(user)
        print("USERS STILL IN ROOM: ", users_all)
        print("Disconnected to Chat Room: ", self.room_name)


    async def receive(self, text_data):
       data= json.loads(text_data)
       message=data['message']
       username=data['username']
       room=data['room']
       
       await self.save_message(username, room, message)
       
       await self.channel_layer.group_send(
           self.room_group_name,
           {
               'type':'chat_message',
               'message': message,
               'username': username,
               "room": room,
           }
       )
       
    async def chat_message(self,event):
        message=event['message']
        username=event['username']
        room=event['room']
        
        await self.send(text_data=json.dumps({
                'message': message,
                'username': username,
                "room": room,
        }))
        
        
    @sync_to_async #store to database
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)
        
        Message.objects.create(user=user, room=room ,content=message)
        
 
# consumers.py



from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .views import get_user_list

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        user_list = get_user_list()

        # Send the user list to the connected client
        await self.send(text_data=json.dumps({'type': 'user_list', 'users': [user.username for user in user_list]}))
        
        
           
        
    