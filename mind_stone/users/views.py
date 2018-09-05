from django.http import JsonResponse
from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from mind_stone.conversations.models import Conversation

@api_view(['GET'])
def get_users(request):
  users = User.objects.all().values()
  return JsonResponse(list(users), safe=False)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_user(request):
  serializer = UserCreateSerializer(data=request.data)
  serializer.is_valid(raise_exception=True)
  new_user = serializer.save()
  all_users = User.objects.all()
  for user in all_users:
    conversation = Conversation.objects.create()
    conversation.users.add(user)
    conversation.users.add(new_user)
    conversation.save()
  return Response(serializer.data, status=status.HTTP_201_CREATED)