
from django.urls import path
from website.views import *
urlpatterns = [
    path('',http_test),
    path('about', http_about)
]
