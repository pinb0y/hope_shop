from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.base import TemplateView

from product_catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from product_catalog.models import Product, Version, Category
from product_catalog.services import get_cashed_categories


class UserLoginRequiredMixin(LoginRequiredMixin):
    login_url = "/users/"
    permission_denied_message = "Только для авторизованных пользователей"


class ProductListView(UserLoginRequiredMixin, ListView):
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        for product in context_data["object_list"]:
            active_version = Version.objects.filter(
                product=product, is_active=True
            ).first()
            product.active_version = active_version
        return context_data


class ProductDetailView(UserLoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(UserLoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UserLoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = ProductFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid and formset.is_valid():
            self.object.save()
            formset.instance = self.object
            formset.save()

            versions = Version.objects.filter(product=self.object, is_active=True)
            if len(versions) > 1:
                form.add_error(None, "Может быть только одна активная версия.")
                return super().form_invalid(form)
            return super().form_valid(form)
        else:
            return self.render_to_response(
                self.get_context_data(form=form, formset=formset)
            )

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perms(
                (
                        "product_catalog.change_description",
                        "product_catalog.change_category",
                        "product_catalog.set_published",
                )
        ):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(UserLoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class ContactTemplateView(UserLoginRequiredMixin, TemplateView):
    template_name = "product_catalog/contacts.html"


class CategoryListView(UserLoginRequiredMixin, ListView):
    model = Category

    def get_queryset(self):
        return get_cashed_categories()