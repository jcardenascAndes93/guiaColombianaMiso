from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

from django.contrib.auth import views as auth_views
from accounts import views

from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'accounts'
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # API Endpoint
    #path('auth/', ObtainAuthToken.as_view()),
    path('api-user/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', views.LoginView.as_view(), name='login'),

]
