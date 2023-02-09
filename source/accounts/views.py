from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from .form import MyUserCreationForm, UserChangeForm, ProfileChangeForm
from .models import Profile


class RegisterView(CreateView):
    model = get_user_model()
    template_name = 'user_create.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:project:index')
        return next_url


class UserChangePasswordView(PasswordChangeView):
    template_name = 'user_change_password.html'

    def get_success_url(self):
        return reverse('accounts:user_view', kwargs={'pk': self.request.user.pk})

