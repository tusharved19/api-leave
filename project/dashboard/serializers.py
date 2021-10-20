from django.db.models import fields
from django.db.models.base import Model
from .models import Department,Employee
from rest_framework.serializers import *
from .views import *
from dashboard import models

class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        
class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
