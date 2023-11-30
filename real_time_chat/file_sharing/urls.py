from django.urls import path
from .views import file_list, file_upload, file_download

urlpatterns = [
    path('files/', file_list, name='file_list'),
    path('upload/', file_upload, name='file_upload'),
    path('download/<int:file_id>/', file_download, name='file_download'),
]
