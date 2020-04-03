from .access_middleware import check_role
from .location_service import save_location , get_locations , get_location_by_id , get_location_weather , get_lat_and_long_by_city
from django.views.decorators.http import require_GET , require_POST
# Create your views here.

@require_POST
@check_role(role=1)
def save(request):
    return save_location(request)

def get_all(request):
    return get_locations(request)

def get_by_id(request , location_id):
    return get_location_by_id(request,location_id)

def get_weather(request , city):
    return get_location_weather(request , city)

def get_cordinates(request , city):
    return get_lat_and_long_by_city(request,city)
