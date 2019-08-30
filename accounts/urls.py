from django.urls import include, path
from rest_framework import routers

from django.contrib.auth import views as auth_views
from accounts import views

app_name = 'accounts'
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users-api/', include('rest_framework.urls', namespace='rest_framework'))
    # path(r'signup/', views.signup_view, name='signup'),
    # path(r'login/', views.login_view, name="login"),
    # path(r'logout/', views.logout_view, name="logout"),
]
