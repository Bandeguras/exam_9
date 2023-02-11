from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.http import urlencode
from webapp.models import Ad
# from webapp.forms import ArticleForm, SimpleSearchForm, ArticleDeleteForm
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
# class ArticleCreateView(LoginRequiredMixin, CreateView):
#     template_name = "article/article_create.html"
#     model = Article
#     form_class = ArticleForm
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#
#
# class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
#     template_name = "article/article_update.html"
#     form_class = ArticleForm
#     model = Article
#     context_object_name = 'article'
#     permission_required = 'webapp.change_article'
#
#     def has_permission(self):
#         return super().has_permission() or self.get_object().author == self.request.user
#
#
# class ArticleDeleteView(PermissionRequiredMixin, DeleteView):
#     template_name = 'article/article_delete.html'
#     model = Article
#     context_object_name = 'article'
#     success_url = reverse_lazy('webapp:index')
#     form_class = ArticleDeleteForm
#     permission_required = 'webapp.delete_article'
#
#     def has_permission(self):
#         return super().has_permission() or self.get_object().author == self.request.user
#
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.form_class(instance=self.object, data=request.POST)
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
