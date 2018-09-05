from rest_framework import viewsets, status
from rest_framework.response import Response
from mind_stone.groups.serializers import GroupSerializer
from mind_stone.groups.models import Group
from mind_stone.conversations.models import Conversation
from mind_stone.groups.serializers import GroupSerializer

class GroupViewSet(viewsets.ModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
  def create(self, request):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    group = serializer.save()
    conversation = Conversation.objects.create(group=group)
    conversation.save()
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

  def get_queryset(self):
    user = self.request.user
    return Group.objects.filter(users__pk=user.pk)

    

    