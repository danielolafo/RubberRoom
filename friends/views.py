from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse

# Create your views here.
class FriendView(APIView):
    def get(self, request, id):
        print('friends.request ', request)
        return HttpResponse('OK', status=204)