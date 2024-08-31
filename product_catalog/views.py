from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from product_catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ("product_name", "description", "price", "image")
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("product_name", "description", "price", "image")
    success_url = reverse_lazy("catalog:product_list")

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


def toggle_activity(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    if product_item.is_active:
        product_item.is_active = False
    else:
        product_item.is_active = True

    product_item.save()

    return redirect(reverse("catalog:product_list"))