from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from pytils.translit import slugify

from product_blog.models import Blog
from product_catalog.views import UserLoginRequiredMixin


class BlogCreateView(UserLoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Blog
    fields = ("title", "body", "preview", "is_published")
    permission_required = "product_blog.add_blog"
    success_url = reverse_lazy("blog:list")

    def form_valid(self, form):
        """Переопределяем метод, чтобы был корректный слаг"""
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogListView(UserLoginRequiredMixin, ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        """Переопределяем метод чтобы отображались только опубликованные статьи"""
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(UserLoginRequiredMixin, DetailView):
    model = Blog

    def get_object(self, queryset=None):
        """Создаем счетчик просмотров"""
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        return self.object


class BlogUpdateView(UserLoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Blog
    fields = ("title", "body", "preview", "is_published")
    permission_required = "product_blog.change_blog"

    def form_valid(self, form):
        """Переопределяем метод чтобы был красивый слаг"""
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        """Переход к блогу после успешного редактирования"""
        return reverse("blog:view", args=[self.kwargs.get("pk")])


class BlogDeleteView(UserLoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:list")
    permission_required = "product_blog.delete_blog"

