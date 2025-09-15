import json

from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rubberroom.models import *
from rubberroom.dtos import WrapperResponse
from rubberroom.serializers import UserInteractionSerializer

# Create your views here.
class FriendView(APIView):
    def get(self, request, id):
        print('friends.request ', request)
        print('friends.id ', id)
        friends_activity = UserInteractions.objects.raw("SELECT ui.* FROM Users u "
                                                        "JOIN user_contact uc ON u.id IN (uc.first_user_id, uc.second_user_id) "
                                                        "JOIN user_interaction ui ON ui.user_id !=u.id "
                                                        "WHERE u.id = %s "
                                                        "ORDER BY ui.registry_date DESC LIMIT 100",[id])
        if len(friends_activity)==0:
            wrapper_response = WrapperResponse()
            wrapper_response.data=None
            wrapper_response.success=False
            wrapper_response.message='No recent friend activity found'
            return HttpResponse(json.dumps(wrapper_response, default=vars), status=404, content_type='application/json')
        serializer = UserInteractionSerializer(friends_activity, many=True)
        return HttpResponse(json.dumps(serializer.data), content_type='application/json', status=200)