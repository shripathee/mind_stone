from django.db import models
from django.contrib.auth.models import User
from mind_stone.groups.models import Group
import datetime

class Conversation(models.Model):
  user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
  group = models.OneToOneField(Group, blank=True, null=True, on_delete=models.CASCADE)

class Thread(models.Model):
  conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)

class Message(models.Model):
  text = models.CharField(max_length=400, default='Hello')
  timestamp = models.DateTimeField(default=datetime.datetime.now())
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  thread = models.ForeignKey(Thread, on_delete=models.CASCADE)