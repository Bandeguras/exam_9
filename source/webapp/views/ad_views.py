from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.http import urlencode
from webapp.models import Ad
from webapp.forms import AdForm
from django.http import JsonResponse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View


class AdIndexViews(ListView):
    template_name = 'ad/index.html'
    context_object_name = 'ads'
    model = Ad
    ordering = ('-created_at',)


#
class AdView(DetailView):
    template_name = 'ad/ad_view.html'
    context_object_name = 'ad'
    model = Ad


#
#
class AdCreateView(LoginRequiredMixin, CreateView):
    template_name = "ad/ad_create.html"
    model = Ad
    form_class = AdForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AdUpdateView(UpdateView):
    template_name = "ad/ad_update.html"
    model = Ad
    form_class = AdForm


class AdDeleteView(DeleteView):
    template_name = 'ad/ad_delete.html'
    model = Ad
    success_url = reverse_lazy('webapp:ad_index')

