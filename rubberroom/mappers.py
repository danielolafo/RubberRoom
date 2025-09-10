from .models import *
from .dtos import AllocationSiteDto, UserDto
from rest_framework import serializers
from mapper.object_mapper import ObjectMapper

class AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllocationSite
        fields = ['id','city','address','owner','ratings','tags']
def to_allocation_dto(allocationSite: AllocationSite):
    dto = AllocationSiteDto()
    dto.id = allocationSite.id
    dto.city=allocationSite.city
    dto.address=allocationSite.address
    dto.tags=allocationSite.tags
    dto.ratings=allocationSite.ratings
    dto.owner = allocationSite.owner.id
    return dto

def to_allocation_site(req_dict):
    allocation_site = AllocationSite()
    allocation_site.tags = req_dict['tags']
    allocation_site.city = req_dict['city']
    allocation_site.ratings = req_dict['ratings']
    allocation_site.address = req_dict['address']
    allocation_site.owner = User(**req_dict['owner'])
    return allocation_site

def user_to_dto(user):
    user_dto = UserDto()
    user_dto.id=user.id
    user_dto.username=user.username
    user_dto.email=user.email
    user_dto.description=user.description
    user_dto.user_rating=user.description
    return user_dto

######################################3

mapper = ObjectMapper()


user_mapping = {
    "id": lambda entity: entity.id,
    "username" : lambda entity: entity.username,
    "user_rating" : lambda entity: entity.user_rating,
    "description" : lambda entity: entity.description,
    "email" : lambda entity: entity.email
}

def to_user_dto(user):
    mapper.create_map(User, UserDto, user_mapping)
    return mapper.map(user, UserDto, user_mapping)