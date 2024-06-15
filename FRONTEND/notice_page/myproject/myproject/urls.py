# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from myapp import views as myapp_views  # Import your app's views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp_views.news_and_notices_view, name='home'),  # Redirect to news and notices view
    path('news/', myapp_views.news_and_notices_view, name='news_and_notices'),  # URL for news and notices
    # Add static and media URL patterns if not included already
]

# Add the following lines to serve static and media files during development
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
