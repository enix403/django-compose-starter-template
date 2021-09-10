from django.urls import path
from .home import index

urlpatterns = [
    path("", index, name="index"),
]