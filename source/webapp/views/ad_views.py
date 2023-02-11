from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.http import urlencode
from webapp.models import Ad
from webapp.forms import AdForm, AdDeleteForm
from django.http import JsonResponse, HttpResponseRedirect

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


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


class AdUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = "ad/ad_update.html"
    model = Ad
    form_class = AdForm
    permission_required = 'webapp.change_ad'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user


class AdDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'ad/ad_delete.html'
    model = Ad
    success_url = reverse_lazy('webapp:ad_index')
    form_class = AdDeleteForm
    permission_required = 'webapp.delete_ad'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(instance=self.object, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        form.instance.status = 'For removal'
        return self.get_success_url()
