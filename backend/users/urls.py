
from django.urls import path, include
from users import views
from .views import RegisterView, LoginView, UserView, LogoutView
# from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register('register', views.RegisterView, basename='register')
# router.register('login', views.LoginView, basename='login')
# router.register('logout', views.LogoutView, basename='logout')
# router.register('user', views.UserView, basename='user')


urlpatterns = [
    # path('', include(router.urls)),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view())
]