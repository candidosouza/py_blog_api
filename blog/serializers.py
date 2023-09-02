from rest_framework import serializers

from blog.models import Category, Comment, Post, UserProfile


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ListPostsUserSerializer(serializers.ModelSerializer):
    writer = serializers.SerializerMethodField()

    def get_writer(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'

    class Meta:
        model = Post
        fields = (
            'title',
            'slug',
            'summary',
            'category',
            'published',
            'created_at',
            'updated_at',
            'writer',
        )


class ListCommentsPostSerializer(serializers.ModelSerializer):
    post = serializers.SerializerMethodField()

    def get_post(self, obj):
        return obj.post.title

    class Meta:
        model = Comment
        fields = (
            'post',
            'name',
            'email',
            'comment',
            'approved',
            'created_at',
            'updated_at',
        )


class ListPostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'slug',
            'summary',
            'category',
            'published',
            'created_at',
            'updated_at',
        )
