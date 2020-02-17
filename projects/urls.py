from projects import views
from django.urls import path
from django.urls import path, include
from rest_framework import routers
from projects import views


router = routers.DefaultRouter()
router.register('api/users/register', views.UserProfileViewSet)
router.register('api/projects', views.ProjectViewSet)
router.register('api/actions', views.ActionViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('api/users/auth', views.AuthenticateUserView.as_view()),
]
