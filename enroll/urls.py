from django.urls import path
from . import views

urlpatterns = [
    path("addandshow", views.add_show),
]