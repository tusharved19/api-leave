from django.shortcuts import render
import requests
from django.conf import settings
from rest_framework.views import APIView
from user.serializers import adminLoginSerializer
from rest_framework.response import Response

class AdminLoginView(APIView):
    def post(self, request):
        serializer = adminLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        try:
            r = requests.post(
                settings.URL_TYPE + "/o/token/",
                data={
                    "grant_type": "password",
                    "username": user.username,
                    "password": request.data["password"],
                    "client_id": settings.CLIENT_ID,
                    "client_secret": settings.CLIENT_SECRET,
                    "scope": "admin",
                },
                verify=False,
            )
            if r.status_code == 200:
                response = r.json()
                details = {}
                details.update(
                    {
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "email": user.email,
                    }
                )
                response.update({"details": details})
                return Response(response)
            else:
                if r.status_code == 500:
                    print(r)
                return Response(r.json(), r.status_code)
        except Exception as e:
            print(e)
            pass
            return Response("error")
class TokenView(APIView):
     def post(self, request):
        try:
            r = requests.post(
                settings.URL_TYPE + "/o/token/",
                data={
                    "grant_type": "refresh_token",
                    "refresh_token": request.data["refresh_token"],
                    "client_id": settings.CLIENT_ID,
                    "client_secret": settings.CLIENT_SECRET,
                    # "scope": "admin",
                },
                verify=False,
            )
            if r.status_code == 200:
                response = r.json()
                #print(response)
                #setRefreshTokenExpiry(response["refresh_token"])
                details = {}
                details.update(
                    {
                        "refresh_token": request.data["refrIsAuthenticatedh_token"]
                    }
                )
                response.update({"details": details})
                return Response(response)
            else:
                if r.status_code == 500:
                    print(r)
                return Response(r.json(), r.status_code)
        except Exception as e:
            print(e)
            pass
            return Response("error")