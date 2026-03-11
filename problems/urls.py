from django.urls import path
from . import views

app_name = 'problems'

urlpatterns = [
    path('', views.problem_list, name='list'),
    path('api/run/', views.run_code, name='run_code'),
    path('<slug:slug>/', views.problem_detail, name='detail'),
]