from rest_framework import serializers
from mind_stone.groups.models import Group

class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = ('id', 'name', 'users')