from django.urls import path


from product_catalog.apps import ProductCatalogConfig
from product_catalog.views import (
    ProductListView,
    ProductUpdateView,
    ProductDetailView,
    toggle_activity,
    ProductCreateView,
    ProductDeleteView,
    ContactTemplateView,
)

app_name = ProductCatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("product_detail/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
    path("activity/<int:pk>", toggle_activity, name="toggle_activity"),
    path("create/", ProductCreateView.as_view(), name="create_product"),
    path("update/<int:pk>", ProductUpdateView.as_view(), name="update_product"),
    path("delete/<int:pk>", ProductDeleteView.as_view(), name="delete_product"),
    path("contacts/", ContactTemplateView.as_view(), name="contacts"),
]
