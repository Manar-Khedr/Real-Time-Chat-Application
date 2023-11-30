from django.db import models
from django.contrib.auth.models import User

#global variable
users_all={}

class Room(models.Model):
    name= models.CharField(max_length=255)
    slug=models.SlugField(unique=True)
    #owner=models.ForeignKey(User, on_delete=models.CASCADE)
    
    
class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('date_added',)
    
