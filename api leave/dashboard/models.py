from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ('department')  
        ordering = ['name']

    def __str__(self):
        return self.name
    

class Employee(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="user")
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name="department",default=1)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,related_name="admin",default=1)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contactnum = models.IntegerField()
    email = models.EmailField(max_length=30, null=True)
    employeeid = models.CharField(_('Employee Id Number'),max_length=5,null=True,blank=True)
    salary = models.FloatField(max_length=10,null=False,default=0)
    allowed_leave = models.IntegerField(null=False ,default=1)
    applied_leaves = models.IntegerField(null=True)
    
    class Meta:
        verbose_name = ('Employee')

    def __str__(self):
        return self.get_full_name

    @property
    def get_full_name(self):
        fullname = ''
        firstname = self.firstname
        lastname = self.lastname
        if (firstname and lastname):
            fullname = firstname + ' ' + lastname
        return fullname

    def save(self, *args, **kwargs):

        user = self.employeeid
        data = user
        self.employeeid = data
        super().save(*args, **kwargs)
        print(self.employeeid)
        
    @property
    def can_apply_leave(self):
        pass

