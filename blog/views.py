from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, viewsets

from blog.models import Category, Comment, Post
from blog.serializers import (
    CategorySerializer,
    CommentSerializer,
    ListCommentsPostSerializer,
    ListCommentsPostSerializerV2,
    ListPostCategorySerializer,
    ListPostsUserSerializer,
    PostSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'put', 'patch']


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ['title', 'created_at', 'updated_at']
    search_fields = ['title', 'summary', 'content']
    filterset_fields = ['category', 'published', 'user']
    http_method_names = ['get', 'post', 'put', 'patch']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ['created_at']
    search_fields = ['post', 'email', 'comment']
    filterset_fields = ['approved']
    http_method_names = ['get', 'post', 'put', 'patch']


class ListPostsUserViewSet(generics.ListAPIView):
    serializer_class = ListPostsUserSerializer
    http_method_names = ['get']

    def get_queryset(self):
        user = User.objects.get(pk=self.kwargs['pk'])
        return Post.objects.filter(user=user)


class ListPostCategoryViewSet(generics.ListAPIView):
    serializer_class = ListPostCategorySerializer
    http_method_names = ['get']

    def get_queryset(self):
        category = Category.objects.get(pk=self.kwargs['pk'])
        return Post.objects.filter(category=category)


class ListCommentsPostViewSet(generics.ListAPIView):
    http_method_names = ['get']
    
    def get_serializer_class(self):
        if self.request.version == '2':
            return ListCommentsPostSerializerV2
        return ListCommentsPostSerializer

    def get_queryset(self):
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Comment.objects.filter(post=post)
