from django.contrib import admin
from django.urls import path, include
from locations import views as location_views



locations_url_patterns = ([
    path('', location_views.save, name="save_locations"),
    path('get-locations/',location_views.get_all,name="get_locations")
])


urlpatterns = [
    path('admin/', admin.site.urls),
    path('locations/',include(locations_url_patterns))
]
