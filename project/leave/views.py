from django.shortcuts import render
from .serializers import LeaveSerializer
from .models import Leave
from rest_framework import viewsets
from .views import * 
from oauth2_provider.contrib.rest_framework import TokenHasScope, OAuth2Authentication
from datetime import datetime, timedelta

class LeaveModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ["admin"]
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
    
    def total_days(self, startdate, enddate):
        oneday = timedelta(days=1)
        startdate = datetime.strptime(startdate, '%Y-%m-%d')
        enddate = datetime.strptime(enddate, '%Y-%m-%d')
        totaldays = 0
        while (startdate <= enddate):
            if not startdate.isoweekday() in (6, 7):
                totaldays += 1
            startdate += oneday
        return totaldays 