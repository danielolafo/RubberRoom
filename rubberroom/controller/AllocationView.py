from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from rest_framework.views import APIView
from django.http import HttpResponse
#from rubberroom.model.AllocationSite import AllocationSite

class AllocationView(APIView):

    def get(self, request):
        print(request.GET.get('city'))
        return HttpResponse("OK")

"""
    def searchById(self):
        pass
"""