
from django.urls import path, include
from .views import AdIndexViews, AdView, AdCreateView, AdUpdateView, AdDeleteView, AdCommentCreateView, CommentDeleteView

app_name = 'webapp'

AddUrl = [
    path('<int:pk>/', AdView.as_view(), name='ad_view'),
    path('update/<int:pk>/', AdUpdateView.as_view(), name='ad_update'),
    path('create', AdCreateView.as_view(), name='ad_create'),
    path('delete/<int:pk>/', AdDeleteView.as_view(), name='ad_delete'),
]

CommentUrl = [
    path('<int:pk>/comment/add/', AdCommentCreateView.as_view(), name='ad_comment_add'),
    path('<int:pk>/comment/delete/', CommentDeleteView.as_view(), name='comment_delete'),

]

urlpatterns = [
    path('', AdIndexViews.as_view(), name='ad_index'),
    path('ad/', include(AddUrl)),
    path('comment/', include(CommentUrl)),

]

