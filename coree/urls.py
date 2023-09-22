from django.conf.urls.static import ImproperlyConfigured
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

api_urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('todo/', include('apps.todo.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)