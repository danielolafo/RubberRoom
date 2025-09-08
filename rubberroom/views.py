from rest_framework.views import APIView
from django.http import HttpResponse
from .models  import AllocationSite, User
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
import json
import logging
from .mappers import *
from .utils import *
from .exceptions import *
import re
from .dtos import UserDto
from mapper.object_mapper import  ObjectMapper

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
class AllocationView(APIView):

    def validate_pagination(self, request):
        city = str(request.GET.get('city'))
        pageNumber = int(request.GET.get('page'))
        pageSize = int(request.GET.get('pageSize'))
        if pageNumber <= 0:
            raise InvalidPageException("The page number cannot be less than 0")
        if pageSize <5 or pageSize > 100:
            raise InvalidPageException("The page size cannot be less than 5 nor greater than 100")

    def get(self, request):
        try:
            logging.info("This is an informational message.")
            city = str(request.GET.get('city'))
            pageNumber = int(request.GET.get('page'))
            pageSize = int(request.GET.get('pageSize'))
            self.validate_pagination(request)
            resp = AllocationSite.objects.all()
            paginator = Paginator(resp, pageSize)
            resp = paginator.page(pageNumber)
            resp = page_to_list(resp)
            resp = [toAllocationDto(item) for item in resp]
            return HttpResponse(json.dumps(resp, default=vars), content_type='application/json')
        except (InvalidPageException, EmptyPage) as ex:
            logging.exception(str(ex))
            logging.exception(ex.__class__)
            print(type(ex)==InvalidPageException)
            if type(ex)==InvalidPageException:
                return HttpResponse(str(ex), content_type='application/json', status=400)
            return HttpResponse('No results found', content_type='application/json', status=404)
        except Exception as ex:
            logging.exception(str(ex))
            logging.exception(ex.__class__)
            return HttpResponse([], content_type='application/json', status=500)

    def post(self, request):
        req = json.loads(request.body.decode('utf-8'))
        logging.info(f"Creating allocation {req}", req)
        req=AllocationSite(**req)
        searchResults = AllocationSite.objects.filter(city=req.city, address=req.address)
        if len(searchResults)>0:
            return HttpResponse([], content_type='application/json', status=400)
        AllocationSite.save(req)
        resp = toAllocationDto(req)
        print(resp.city+" "+resp.address)
        return HttpResponse(json.dumps(resp, default=vars), content_type='application/json', status=201)

class UserView(APIView):

    def post(self, request):
        req = json.loads(request.body.decode('utf-8'))
        user = User(**req)
        user_validation = self.validate_user(user)
        if(not user_validation.is_valid):
            logging.info("post %s", json.dumps(user_validation, default=vars))
            return HttpResponse(json.dumps(user_validation, default=vars), content_type='application/json', status=400)
        #User.save(user)
        user.save()
        user_dto = UserDto()
        user_dto = user_to_dto(user)
        return HttpResponse(json.dumps(user_dto, default=vars), content_type='application/json', status=201)

    def is_user_existent(self,user):
        logging.info("is_user_existsten %s",json.dumps(user, default=vars))
        db_users = User.objects.filter(Q(email=user.email) | Q(username=user.username))
        if db_users is not None and len(db_users)>0:
            logging.exception("is_user_existent : Exception : Username or email exists")
            raise Exception("Username or email exists")

    def validate_user(self, user):
        logging.info("validate_user: user %s",json.dumps(user, default=vars))
        try:
            self.is_user_existent(user)
            email_resp = self.validate_email(user)
            if(email_resp.is_valid):
                val_resp = ValidationResponseBuilder()
                return val_resp.build_valid(True).build_message('User is valid').build()
            else:
                return ValidationResponse.ValidationResponseBuilder(self).build_valid(False).build_message('User is invalid').build()
        except Exception as ex:
            logging.exception("validate_user : %s", ex)
            valResp = ValidationResponse(False,str(ex))
            return valResp

    def validate_email(self, user):
        email_pattern = r"^[a-zA-Z0-9]{1,10}@[a-zA-Z0-9]{1,10}\.[a-zA-Z]{3}$"
        try:
            if re.match(email_pattern, user.email):
                return ValidationResponse(True, "User is valid")
            return ValidationResponse.ValidationResponseBuilder().build_valid(False).build_message('The email is invalid').build()
        except Exception as ex:
            logging.error("Exception : ",ex)
            raise InvalidEmailException("The email is invalid")

class FeedView(APIView):

    """
    Get a list of possible interesting allocations for an user based on their friends
    and interest activity.
    """
    def get(self, user_id):
        #Call Kafka module
        try:
            pass
        except:
            raise Exception("Not numeric user id")