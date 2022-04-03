from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('profiles', views.UserProfileViewSet)

urlpatterns = [
    path('login', views.UserLoginApiView.as_view(), name='login'),
    path('', views.home, name='home'),
    path('', include(router.urls))


]
