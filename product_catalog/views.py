from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.base import TemplateView

from product_catalog.forms import ProductForm
from product_catalog.models import Product, Version


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        for product in context_data['object_list']:
            active_version = Version.objects.filter(product=product, is_active=True).first()
            product.active_version = active_version
        return context_data


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")




class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


# def toggle_activity(request, pk):
#     product_item = get_object_or_404(Product, pk=pk)
#     if product_item.is_active:
#         product_item.is_active = False
#     else:
#         product_item.is_active = True
#
#     product_item.save()
#
#     return redirect(reverse("catalog:product_list"))


class ContactTemplateView(TemplateView):
    template_name = "product_catalog/contacts.html"
