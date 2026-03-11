from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.quiz_list, name='list'),
    path('<int:quiz_id>/', views.quiz_detail, name='detail'),
    path('<int:quiz_id>/start/', views.start_quiz, name='start'),
    path('<int:quiz_id>/submit/', views.submit_quiz, name='submit'),
    path('result/<int:attempt_id>/', views.quiz_result, name='result'),
    path('daily/', views.daily_quiz, name='daily'),
]