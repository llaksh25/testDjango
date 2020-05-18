from django.urls import path
from ExcelHandler.views import post_excel, open_pyxl

urlpatterns = [
    path('postOpenpyxl/', post_excel, name="postOpenpyxl"),
    path('getOpenpyxl/', open_pyxl, name="getOpenpyxl"),
]