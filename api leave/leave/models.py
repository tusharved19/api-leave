from django.db import models
from django.utils.translation import ugettext as _
from dashboard.models import Employee

SICK = 'sick'
CASUAL = 'casual'
EMERGENCY = 'emergency'
STUDY = 'study'

LEAVE_TYPE = (
(SICK,'Sick Leave'),
(CASUAL,'Casual Leave'),
(EMERGENCY,'Emergency Leave'),
(STUDY,'Study Leave'),
)

DAYS = 10
STATUS=(
    ("1", "pending"),
    ("2", "approved"),
    ("3", "rejected"),
    ("4", "cancelled"),
)

class Leave(models.Model):
	employee = models.ForeignKey(Employee,on_delete=models.CASCADE,default=1)
	startdate = models.DateField(verbose_name=_('Start Date'),null=True,blank=False)
	enddate = models.DateField(verbose_name=_('End Date'),null=True,blank=False)
	leavetype = models.CharField(choices=LEAVE_TYPE,max_length=25,default=SICK,null=True,blank=False)
	reason = models.CharField(verbose_name=_('Reason for Leave'),max_length=255,null=True,blank=True)
	totaldays = models.PositiveIntegerField(verbose_name=_('total days'),default=DAYS,null=True,blank=True)
	status = models.CharField(max_length=15,default=1,choices = STATUS) #pending,approved,rejected,cancelled

	class Meta:
		verbose_name = _('Leave')



	def __str__(self):
		return ('{0} - {1}'.format(self.leavetype,self.employee))
