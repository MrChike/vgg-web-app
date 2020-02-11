from projects import views
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects import views


router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('users/register', views.CreateUserView.as_view()),
    path('users/auth', views.AuthenticateUserView.as_view()),
]
