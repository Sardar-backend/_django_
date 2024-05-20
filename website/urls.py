from django.urls import path
from website.views import *



urlpatterns = [
    path('',http_test, name="index"),
    path('about', http_about, name="about"),
    path('contact', http_contact , name="contact")
]
