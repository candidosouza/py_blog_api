from django.contrib import admin
from django.urls import include, path

from blog.urls import urlpatterns as blog_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(blog_urls)),
]
