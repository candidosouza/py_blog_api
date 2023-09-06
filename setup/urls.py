from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from blog.urls import urlpatterns as blog_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(blog_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
