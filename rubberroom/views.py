from rest_framework.views import APIView
from django.http import HttpResponse
from .models  import AllocationSite
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage
import json
import logging
from .mappers import toAllocationDto, AllocationSerializer
from .utils import *
from .exceptions import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
class AllocationView(APIView):

    def get(self, request):
        try:
            logging.info("This is an informational message.")
            print(request.GET.get('city'))
            city = str(request.GET.get('city'))
            pageNumber = int(request.GET.get('page'))
            pageSize = int(request.GET.get('pageSize'))
            resp = AllocationSite.objects.all()
            paginator = Paginator(resp, pageSize)
            resp = paginator.page(pageNumber)
            # resp = [toAllocationDto(x) for x in resp]
            resp = page_to_list(resp)
            resp = [toAllocationDto(item) for item in resp]
            return HttpResponse(json.dumps(resp, default=vars), content_type='application/json')
        except (InvalidPageException, EmptyPage) as ex:
            logging.exception(str(ex))
            logging.exception(ex.__class__)
            return HttpResponse([], content_type='application/json', status=400)
        except Exception as ex:
            logging.exception(str(ex))
            logging.exception(ex.__class__)
            return HttpResponse([], content_type='application/json', status=500)

    def post(self, request):
        #logging.info(f"Creating allocation {request}", {request})
        req = json.loads(request.body.decode('utf-8'))
        logging.info(f"Creating allocation {req}", req)
        req=AllocationSite(**req)
        logging.info(f"Creating allocation {req}")
        logging.info("Creating allocation "+ serializers.serialize('json', [req]))

        searchResults = AllocationSite.objects.filter(city=req.city, address=req.address)
        print('searchResults size ',len(searchResults))
        if len(searchResults)>0:
            return HttpResponse([], content_type='application/json', status=400)
        AllocationSite.save(req)
        resp = toAllocationDto(req)
        print(resp.city+" "+resp.address)
        return HttpResponse(json.dumps(resp, default=vars), content_type='application/json', status=201)
