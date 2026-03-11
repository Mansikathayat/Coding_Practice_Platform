from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('progress/', views.progress, name='progress'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('mini-projects/', views.mini_projects, name='mini_projects'),
]