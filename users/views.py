import secrets

from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView

from config.settings import EMAIL_HOST_USER
from product_catalog.views import UserLoginRequiredMixin
from users.forms import UserRegisterForm, UserProfileForm, ResetPasswordForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        send_mail(
            subject="Подтверждение почты",
            message=f"Добрый день! Перейдите по ссылке для подтверждения {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


class ProfileView(UserLoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy("catalog:product_list")

    def get_object(self, queryset=None):
        return self.request.user


def email_verification(requests, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class UserResetPasswordView(UserLoginRequiredMixin, PasswordResetView):
    form_class = ResetPasswordForm
    template_name = "users/reset_password.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        try:
            user = User.objects.get(email=email)
            if user:
                password = User.objects.make_random_password(length=10)
                user.set_password(password)
                user.save()
                send_mail(
                    subject="Сброс пароля",
                    message=f" Ваш новый пароль {password}",
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[user.email],
                )
            return redirect(reverse("users:login"))
        except:
            return redirect(reverse("users:no_email"))


class NotMailPageView(UserLoginRequiredMixin, TemplateView):
    template_name = "users/no_email.html"
