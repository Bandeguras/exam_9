from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from .form import MyUserCreationForm, UserChangeForm
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


class UserDetailView(LoginRequiredMixin, DetailView, MultipleObjectMixin):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        ads = self.get_object().ads.all()
        for i in ads:
            if i.user == self.request.user:
                ads = self.get_object().ads.all().exclude(status='For removal')
            else:
                ads = self.get_object().ads.all().filter(status='published')
        return super().get_context_data(object_list=ads, **kwargs)

class UserChangeView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.get_object().pk})


class UserChangePasswordView(PasswordChangeView):
    template_name = 'user_change_password.html'

    def get_success_url(self):
        return reverse('accounts:user_view', kwargs={'pk': self.request.user.pk})

