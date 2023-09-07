from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from blog.urls import urlpatterns as blog_urls

urlpatterns = [
    path('blog-platform-admin/', admin.site.urls),
    path('api/', include(blog_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
