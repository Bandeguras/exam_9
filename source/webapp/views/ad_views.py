from urllib.parse import urlencode

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from webapp.models import Ad
from webapp.forms import AdForm, SimpleSearchForm
from django.http import JsonResponse, HttpResponseRedirect, HttpResponseNotFound

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class AdIndexViews(ListView):
    template_name = 'ad/index.html'
    context_object_name = 'ads'
    model = Ad
    ordering = ('-created_at',)
    paginate_by = 3

    def get_queryset(self):
        queryset = Ad.objects.filter(status='published')
        if self.search_value:
            queryset = queryset.filter(Q(title__icontains=self.search_value)).filter(status='published')
        return queryset

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context


class AdView(DetailView):
    template_name = 'ad/ad_view.html'
    context_object_name = 'ad'
    model = Ad

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ad = self.object
        comments = ad.comments.order_by('-created_at')
        context['comments'] = comments
        return context


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

    def form_valid(self, form):
        if self.get_object().status == 'rejected':
            return HttpResponseNotFound('<h1>you can not update rejected ad only delete</h1>')
        else:
            form.instance.status = 'on moderate'
            return super().form_valid(form)

    def has_permission(self):
        return self.get_object().user == self.request.user


class AdDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'ad/ad_delete.html'
    model = Ad
    success_url = reverse_lazy('webapp:ad_index')


    def has_permission(self):
        return self.get_object().user == self.request.user

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.status = 'For removal'
        self.object.save()
        return redirect('webapp:ad_index')
