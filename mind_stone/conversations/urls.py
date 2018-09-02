from django.urls import re_path, path
from mind_stone.conversations import views

urlpatterns = [
  path('', views.fetch_conversation),
  re_path(r'(?P<pk>[0-9]+)/$', views.update_conversation),
]