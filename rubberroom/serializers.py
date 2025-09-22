from .models import *
from rest_framework import serializers

class AllocationSiteSerializer():

    def serialize(self, allocation_site_dto):
        return allocation_site_dto.model_dump()

class UserInteractionSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInteractions
        fields =  ['id','registry_date', 'activity_entity', 'activity_id',  'user_id']