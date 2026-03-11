from django.urls import path, include

urlpatterns = [
    path('problems/', include('apps.problems.api_urls')),
    path('submissions/', include('apps.submissions.api_urls')),
    path('users/', include('apps.users.api_urls')),
    path('contests/', include('apps.contests.api_urls')),
]