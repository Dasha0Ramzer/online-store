from tkinter.font import names

from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, ProductDetailView, AddProductView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("add_product/", AddProductView.as_view(), name="add_product"),
    path("product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("product_delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
]
