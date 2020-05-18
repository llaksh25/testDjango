from django.urls import path
from emailHandler.views import post_email

urlpatterns = [
    path('postMail/', post_email, name="postMail"),
]