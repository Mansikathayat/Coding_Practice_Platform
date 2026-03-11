from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from chatbot_views import chatbot_view, chat_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('problems/', include('problems.urls')),
    path('submissions/', include('submissions.urls')),
    path('users/', include('users.urls')),
    path('quiz/', include('quiz.urls')),
    path('chatbot/', chatbot_view, name='chatbot'),
    path('api/chat/', chat_api, name='chat_api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)