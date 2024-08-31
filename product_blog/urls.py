from django.urls import path

from product_blog.apps import ProductBlogConfig
from product_blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = ProductBlogConfig.name

urlpatterns = [
    path("", BlogListView.as_view(), name="list"),
    path("blog_detail/<int:pk>", BlogDetailView.as_view(), name="detail"),
    path("create/", BlogCreateView.as_view(), name="create"),
    path("update/<int:pk>", BlogUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", BlogDeleteView.as_view(), name="delete"),
]