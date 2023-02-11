
from django.urls import path, include
from .views import AdIndexViews, AdView


app_name = 'webapp'

AddUrl = [
    path('<int:pk>/', AdView.as_view(), name='ad_view'),
]

urlpatterns = [
    path('', AdIndexViews.as_view(), name='ad_index'),
    path('ad/', include(AddUrl)),
]