from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User


def main_page(request):
    return render(request, template_name='eb_tests/base/base.html')


class RegistrationView(CreateView):
    form_class = forms.RegForm
    template_name = 'eb_tests/registration.html'

    def get_success_url(self, **kwargs):
        if kwargs == None:
            return reverse_lazy('reg_done')
        return reverse_lazy('reg_done')


class UserLoginView(LoginView):
    template_name = 'eb_tests/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = reverse_lazy('main')
        return context

class UserLogoutView(LogoutView, LoginRequiredMixin):
    next_page = 'logout_done'


class LogOutDone(TemplateView):
    template_name = 'eb_tests/logout.html'


class RegisterDoneView(TemplateView):
    template_name = 'eb_tests/register_done.html'


class LKView(TemplateView):
    template_name = 'eb_tests/lk.html'


class SettingsView(TemplateView):
    template_name = 'eb_tests/settings.html'


class ChangeUserInfoView(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = User
    form_class = forms.ChangeUserInfo
    success_message = 'Личные данные изменены'
    success_url = reverse_lazy('settings')
    template_name = 'eb_tests/change_info.html'


class ChangePasswordView(PasswordChangeView):
    template_name = 'eb_tests/change_password.html'
    success_url = reverse_lazy('pass_change_done')


class ChangePasswordDoneView(PasswordChangeDoneView):
    template_name = 'eb_tests/password_change_done.html'
