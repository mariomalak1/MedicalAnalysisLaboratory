from django.urls import path
from . import views


urlpatterns = [
    path("homepage/", views.homePage, name = "homepage"),
]