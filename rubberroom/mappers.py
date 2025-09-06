from .models import AllocationSite, User
from .dtos import AllocationSiteDto, UserDto
from rest_framework import serializers
from mapper.object_mapper import ObjectMapper

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