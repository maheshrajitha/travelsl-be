from .access_middleware import check_role
from .location_service import save_location , get_locations
from django.views.decorators.http import require_GET , require_POST
# Create your views here.

@require_POST
@check_role(role=1)
def save(request):
    return save_location(request)

def get_all(request):
    return get_locations(request)
