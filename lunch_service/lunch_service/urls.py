from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from lunch_service import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
    path('accounts/', include('accounts.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)