from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.ProblemListAPIView.as_view(), name='api-problem-list'),
    path('<int:pk>/', api_views.ProblemDetailAPIView.as_view(), name='api-problem-detail'),
]