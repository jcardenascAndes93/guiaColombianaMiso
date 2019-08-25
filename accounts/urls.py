from django.urls import path
from django.contrib.auth import views as auth_views

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path(r'signup/', views.signup_view, name='signup'),
    path(r'login/', views.login_view, name="login"),
    # url(r'^login/$', auth_views.LoginView.as_view(template_name="useraccounts/login.html"), name="login"),

]
