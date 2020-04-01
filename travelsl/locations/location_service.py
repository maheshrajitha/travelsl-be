from django.http import JsonResponse , HttpResponse
import json
from .models import Location, LocationImages , Images
from .photo_upload import upload_file_to_azure
from django.core.serializers import serialize

# @check_role(1)
#@require_POST
def save_location(request):
    request_body = json.loads(request.body)
    location = Location()
    location.description=request_body.get("description")
    location.name=request_body.get("name")
    location.city=request_body.get("city")
    images = Images(url=upload_file_to_azure(request_body.get("image")))
    images.save()
    location.images.add(images)
    return JsonResponse({'OK': 'OK'}, status=201)

def get_locations(request):
    # location_list = Location.objects.all()
    # locations = []
    # for location in location_list :
    #     images=LocationImages.objects.filter(location=location.id)
    #     image_list = list()
    #     for image in images :
    #         image_list.append(image.url)
    #     location_info = {
    #         'name' : location.name,
    #         'description' : location.description,
    #         'id' : str(location.pk),
    #         'images' : image_list,
    #         'city': location.city
    #     }
    #     locations.append(location_info)
    location_list = Location.objects.all()
    locations = list()
    for location in location_list :
        images_list = list()
        for image in location.images.all() :
            images_list.append(image.url)
        location = {
            "name" : location.name,
            "description": location.description,
            "images" : images_list,
            "id" : str(location.id),
            "city" : location.city

        }
        locations.append(location)
    return HttpResponse([locations],content_type="application/json")
