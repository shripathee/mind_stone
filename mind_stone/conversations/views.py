from mind_stone.conversations.models import Message, Thread, Conversation
from django.contrib.auth.models import User
from django.http import JsonResponse
from mind_stone.groups.models import Group
from rest_framework import viewsets
from rest_framework.decorators import api_view
import datetime

def serialize(conversation):
  if conversation is not None:
    threads = Thread.objects.filter(conversation=conversation)
    response = {
      'id': conversation.id,
      'threads': []
    }
    if threads:
      for thread in threads:
        messages = Message.objects.filter(thread=thread)
        response['threads'].append({
          'messages': list(map(lambda x: {
            'text': x.text,
            'author': x.author.username,
            'timestamp': x.timestamp
          }, messages))
        })
    return JsonResponse(response)

@api_view(['PATCH'])
def update_conversation(request, pk=None):
  conversation = Conversation.objects.get(pk=pk)
  user = request.user
  text = request.data.get('message')
  timestamp = datetime.datetime.now()
  thread_id = request.data.get('thread_id')
  if thread_id:
    thread = Thread.objects.get(pk=thread_id)
  else:
    thread = Thread.objects.create(conversation=conversation)
    thread.save()
  message = Message.objects.create(author=user, text=text, timestamp=timestamp, thread=thread)
  message.save()
  return serialize(conversation)

@api_view(['GET'])
def fetch_conversation(request):
  query_params = request.query_params
  current_user = request.user
  user_id = query_params.get('user_id', None)
  group_id = query_params.get('group_id', None)
  if user_id is not None:
    user = User.objects.get(pk=user_id)
    for conv in Conversation.objects.filter(users__pk=current_user.pk):
      if current_user.pk is user.pk:
        if len(conv.users.all()) is 1:
          conversation = conv
      else:
        if user in conv.users.all():
          conversation = conv
  elif group_id is not None:
    group = Group.objects.get(pk=group_id)
    conversation = Conversation.objects.get(group=group)
  return serialize(conversation)
