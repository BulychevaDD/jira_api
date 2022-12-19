from django.conf.urls.static import static
from django.urls import path, include

from jira_api import settings

urlpatterns = [
    path('users/', include('users.urls')),
    path('tasks/', include('tasks.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
