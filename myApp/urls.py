from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('logout/', views.Logout, name="logout"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('profile/', views.profile, name="profile"),
]
