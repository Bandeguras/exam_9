
from django.urls import path, include
from .views import AddIndexViews


app_name = 'webapp'

AddUrl = [

]

urlpatterns = [
    path('', AddIndexViews.as_view(), name='ad_index'),
]