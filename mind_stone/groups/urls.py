from mind_stone.groups.views import GroupViewSet
from django.urls import path
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'', GroupViewSet)
urlpatterns = router.urls