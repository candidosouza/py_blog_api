from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from blog.models import Category, Comment, Post
from blog.serializers import (
    CategorySerializer,
    CommentSerializer,
    ListCommentsPostSerializer,
    ListPostCategorySerializer,
    ListPostsUserSerializer,
    PostSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


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


class ListPostsUserViewSet(generics.ListAPIView):
    serializer_class = ListPostsUserSerializer

    def get_queryset(self):
        user = User.objects.get(pk=self.kwargs['pk'])
        return Post.objects.filter(user=user)


class ListPostCategoryViewSet(generics.ListAPIView):
    serializer_class = ListPostCategorySerializer

    def get_queryset(self):
        category = Category.objects.get(pk=self.kwargs['pk'])
        return Post.objects.filter(category=category)


class ListCommentsPostViewSet(generics.ListAPIView):
    serializer_class = ListCommentsPostSerializer

    def get_queryset(self):
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Comment.objects.filter(post=post)
