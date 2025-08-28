from .models import AllocationSite
from .dtos import AllocationSiteDto
from rest_framework import serializers

class AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllocationSite
        fields = '__all__'
def toAllocationDto(allocationSite: AllocationSite):
    dto = AllocationSiteDto()

    dto.city=allocationSite.city
    dto.address=allocationSite.address
    dto.tags=allocationSite.tags
    dto.ratings=allocationSite.ratings

    return dto