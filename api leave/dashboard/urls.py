from django.urls import path
from .views import *
from rest_framework import routers
from django.urls import path,include
from dashboard import views

router = routers.DefaultRouter()
router.register(r'department',DepartmentModelViewSet)
router.register(r'employee', EmployeeModelViewSet)

app_name = 'dashboard'
urlpatterns = [
    path('', include(router.urls)),
    path('salary/<int:id>/',views.EmployeeSalary.as_view(), name = 'salary'),
    path('o', include('oauth2_provider.urls', namespace='oauth2_provider')),
] 
   