from django.contrib import admin

from dashboard.models import Department, Employee

# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)
