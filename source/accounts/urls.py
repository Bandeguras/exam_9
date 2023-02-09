from django.urls import path
from accounts.views import RegisterView, UserChangePasswordView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', RegisterView.as_view(), name='create'),
    path('user/change/password/', UserChangePasswordView.as_view(), name='user_change_password'),

]