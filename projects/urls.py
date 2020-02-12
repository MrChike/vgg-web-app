from projects import views
from django.urls import path
from django.urls import path, include
from rest_framework import routers
from projects import views


router = routers.DefaultRouter()
router.register('users/register', views.UserProfileViewSet)
router.register('projects', views.ProjectViewSet)
# router.register(
#     'users/auth', views.AuthenticateUserView.as_view(), basename='users/auth')


urlpatterns = [
    path('', include(router.urls)),
    # path('users/register', views.CreateUserView.as_view()),
    path('users/auth', views.AuthenticateUserView.as_view()),
]
