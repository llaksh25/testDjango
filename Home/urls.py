from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_view, name="post"),
    path('get/', views.get_view, name="get"),
    path('getOne/<str:param>', views.get_one, name="getOne"),
    path('putDelete/', views.put_delete, name="putDelete"),
    path('joinTable/', views.join, name="joinTable"),

]