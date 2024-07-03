from app.views import *
from django.urls import path

# from . import views


urlpatterns = [
    path("index", home_page),
]
