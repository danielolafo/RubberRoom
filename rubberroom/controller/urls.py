from .AllocationView import *

#router = routers.SimpleRouter()

urlpatterns = [
    path("allocation/", AllocationView),
    path("admin/", admin.site.urls),
]