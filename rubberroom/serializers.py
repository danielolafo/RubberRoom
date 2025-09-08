class AlloationSiteSerializer():

    def serialize(self, allocation_site_dto):
        return allocation_site_dto.model_dump()