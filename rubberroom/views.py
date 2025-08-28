from rest_framework.views import APIView
from django.http import HttpResponse
from .models  import AllocationSite
from django.core import serializers
import json
import logging
from .mappers import toAllocationDto, AllocationSerializer

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
class AllocationView(APIView):

    def get(self, request):
        logging.info("This is an informational message.")
        print(request.GET.get('city'))
        asi = AllocationSite()
        asi.city='Oklahoma'
        asi.address="Stret 123"
        AllocationSite.save(asi)
        resp=AllocationSite.objects.all()
        tmp=list(resp)
        print(tmp[2])
        print(tmp[2].city)
        #print(serializers.serialize('json',tmp[2]))
        resp2 = serializers.serialize('json',resp)
        print(type(resp2))
        return HttpResponse(resp2, content_type='application/json')

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

"""
    def searchById(self):
        pass
"""