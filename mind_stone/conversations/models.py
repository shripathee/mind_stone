from django.db import models
from django.contrib.auth.models import User
from mind_stone.groups.models import Group
from django.utils.timezone import now

class Conversation(models.Model):
  users = models.ManyToManyField(User, blank=True, null=True)
  group = models.OneToOneField(Group, blank=True, null=True, on_delete=models.CASCADE)

class Thread(models.Model):
  conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)

class Message(models.Model):
  text = models.CharField(max_length=400, default='')
  timestamp = models.DateTimeField(default=now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  thread = models.ForeignKey(Thread, on_delete=models.CASCADE)