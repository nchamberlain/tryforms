from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    # path "" means the root of contact/ in urls.py in tryforms (outer urls.py)
    path("", views.contact, name="contact"),
    path("add/", views.client, name="client"),
]