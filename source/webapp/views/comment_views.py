from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import CommentForm
from webapp.models import Comment, Ad


class AdCommentCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'comment/create.html'
    model = Comment
    form_class = CommentForm

    def has_permission(self):
        ad = get_object_or_404(Ad, pk=self.kwargs.get('pk'))
        return ad.user != self.request.user

    def get_success_url(self):
        return reverse('webapp:ad_view', kwargs={'pk': self.object.ad.pk})

    def form_valid(self, form):
        ad = get_object_or_404(Ad, pk=self.kwargs.get('pk'))
        form.instance.ad = ad
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentDeleteView(PermissionRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment

    def has_permission(self):
        ad = get_object_or_404(Ad, pk=self.kwargs.get('pk'))
        return ad.user == self.request.user

    def test_func(self):
        return self.request.user.has_perm('webapp.delete_comment') or self.get_object().author == self.request.user

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:ad_view', kwargs={'pk': self.object.ad.pk })

