from django.db.models import fields
from .models import Leave
from rest_framework.serializers import *

from leave import models

class LeaveSerializer(ModelSerializer):
    class Meta:
        model = Leave
        fields = '__all__'
        
