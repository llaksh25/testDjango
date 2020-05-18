from django.urls import path
from imageFile.views import post_image, get_view, delete

urlpatterns = [
    path('postImg/', post_image, name="postImg"),
    path('getImageFile/', get_view, name="getImageFile"),
    path('deleteFile/', delete, name="deleteFile")
]