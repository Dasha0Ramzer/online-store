from tkinter.font import names

from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, home_view

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("home_view/", home_view, name="home_view"),
]
