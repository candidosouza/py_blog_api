from django.urls import include, path
from rest_framework import routers

from blog.views import (
    CategoryViewSet,
    CommentViewSet,
    ListCommentsPostViewSet,
    ListPostCategoryViewSet,
    ListPostsUserViewSet,
    PostViewSet,
)

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='Category')
router.register(r'posts', PostViewSet, basename='Post')
router.register(r'comments', CommentViewSet, basename='Comment')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'user/<int:pk>/posts/',
        ListPostsUserViewSet.as_view(),
        name='list_posts_user',
    ),
    path(
        'category/<int:pk>/posts/',
        ListPostCategoryViewSet.as_view(),
        name='list_posts_category',
    ),
    path(
        'post/<int:pk>/comments/',
        ListCommentsPostViewSet.as_view(),
        name='list_comments_post',
    ),
]
