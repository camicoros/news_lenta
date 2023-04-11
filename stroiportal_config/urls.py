from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


admin.site.site_header = settings.WEBSITE_NAME

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
