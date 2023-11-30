
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')), #Dont forget the include
    path('rooms/', include('room.urls')),
    path("admin/", admin.site.urls),
    path('file_sharing/', include('file_sharing.urls')),
]
