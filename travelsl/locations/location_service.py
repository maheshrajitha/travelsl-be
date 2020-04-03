from django.http import JsonResponse , HttpResponse
import json
from .models import Location, LocationImages , Images
from .photo_upload import upload_file_to_azure
import requests
from mapbox import Geocoder

# @check_role(1)
#@require_POST
def save_location(request):
    request_body = json.loads(request.body)
    location = Location()
    location.description=request_body.get("description")
    location.name=request_body.get("name")
    location.city=request_body.get("city")
    images = Images(url=upload_file_to_azure(request_body.get("image")))
    location.save()
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


def get_location_by_id(request , location_id):
    location = Location.objects.get(id=location_id)
    if location is not None :
        images_list = list()
        for image in location.images.all():
            images_list.append(image.url)
        location_by_id = {
            "name" : location.name,
            "description": location.description,
            "images" : images_list,
            "id" : str(location.id),
            "city" : location.city
        }
        print(location_by_id)
        return HttpResponse([location_by_id],content_type="application/json")

def get_location_weather(request , city):
    response_fro_open_weather_api = requests.get("http://api.openweathermap.org/data/2.5/weather?q={},LK&units=metric&appid=6432bcdf6dc50b554d8b96cc9833e991".format(city))
    #print(response_fro_open_weather_api.json())
    if response_fro_open_weather_api.status_code == 200 :
        json_response = response_fro_open_weather_api.json()
        weather = {
            "description" : json_response.get("weather")[0].get("description"),
            "icon" : "http://openweathermap.org/img/w/{}.png".format(json_response.get("weather")[0].get("icon")),
            "temp" : json_response.get("main").get("temp"),
        }
        return HttpResponse([weather],content_type="application/json")
    else:
        return JsonResponse({"ERROR_OCCURED":True},status=500)

def get_lat_and_long_by_city(request,city):
    geo_coder = Geocoder(access_token="pk.eyJ1IjoibWFoZXNoLXJhaml0aGEiLCJhIjoiY2s3Y2EyNG0zMGt2azNrbXI3MGhobGsyYiJ9.L5blu4mfiCDmlpcRsR9MVw")
    response = geo_coder.forward("{} ,LK".format(city))
    lat_and_long = {
        "long": response.json().get("features")[0].get("center")[0],
        "lat": response.json().get("features")[0].get("center")[1]
    }
    return HttpResponse([lat_and_long],content_type="application/json")
