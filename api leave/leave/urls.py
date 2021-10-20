from rest_framework import routers
from .views import *
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r'leave',LeaveModelViewSet)

urlpatterns = [
     path('', include(router.urls)),
]