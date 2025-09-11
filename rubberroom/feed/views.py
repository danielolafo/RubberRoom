from rest_framework.views import APIView
from ..models import AllocationSite

class FeedView(APIView):
    def get(self, request, user_id):
        """
        Generate and return and user feed based on its previous interactions, activity and
        contacts activities
        """
        AllocationSite.objects.raw("SELECT * FROM allocation_site");
        pass