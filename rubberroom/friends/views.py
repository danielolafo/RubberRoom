import json

from rest_framework.views import APIView
from django.http import HttpResponse
from ..models import UserContact, UserInteractions
from ..dtos import WrapperResponse

class FriendView(APIView):

    def get(self, request, user_id):
        """
        Recover the main user friend activity
        """
        #friends = UserContact.objects.filter(user_id==user_id)#.order_by('-')[:100]
        #friends_content = UserInteractions.objects.select_related('user_id').filter(user_id)
        friends_content = UserInteractions.objects.raw("SELECT ui.* FROM Users u "
                                                       "JOIN User_Contact uc ON u.id = uc.first_user_id OR u.id = uc.second_user_id "
                                                       "JOIN User_Interaction ui ON ui.id IN (uc.id, uc.second_user_id)WHERE u.id !=ui.user_id")
        if len(friends_content)==0:
            wrapper_response = WrapperResponse()
            wrapper_response.data=None
            wrapper_response.message='No user friends recent activity found'
            wrapper_response.success=False
            return HttpResponse(json.dumps(wrapper_response, default=vars), status=404)
        return HttpResponse(json.dumps(friends_content, default=vars), status=200)

class FriendInteractionView(APIView):

    def get(self, request, user_id):

        pass