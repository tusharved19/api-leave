from django.contrib.auth.models import User
from django.db import models
from django.db.models.query import QuerySet
from leave.models import Leave
from rest_framework import viewsets
from .serializers import DepartmentSerializer,EmployeeSerializer
from .models import Department, Employee 
from oauth2_provider.contrib.rest_framework import TokenHasScope, OAuth2Authentication
from rest_framework.views import APIView
from rest_framework.response import Response


class DepartmentModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ["Employee"]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
  
class EmployeeModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ["admin"]
   
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class EmployeeSalary(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ["admin"]

    def get(self,request,id=None):
        emp = Employee.objects.filter(id = id)        
        data = []
        for i in emp:
            emp = {}
            salary = Employee_Salary(i)
            emp["id"] = i.id
            emp["user"] = i.user.id
            emp["firstname"] = i.firstname
            emp["admin"] = i.admin.id
            emp["allowed_leave"] = i.allowed_leave
            emp["actual_salary"] = salary["actual_salary"]
            emp["final_salary"] = salary["final_salary"]
            emp["applied_leaves"] = i.applied_leaves
            data.append(emp)
            return Response(data)    
    
def Employee_Salary(i):
    allowed_leave = 1
    queryset = Leave.objects.filter(id = i.id)
    pay = i.salary
    daily_amount = i.salary/30
    leaves = queryset.count() + allowed_leave 
    amount = leaves * daily_amount
    pay = i.salary - amount
      
    print({"actual_salary" : i.salary , "final_salary":round(pay,2)})
    return ({"actual_salary" : i.salary , "final_salary":round(pay,2)})



