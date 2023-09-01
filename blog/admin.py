from django.contrib import admin

from blog.models import Category, Post, UserProfile, Comment


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'type_user',
        'is_active',
        'last_seen',
        'created_at',
        'updated_at',
    )
    list_filter = ('type_user', 'is_active', 'created_at', 'updated_at')
    search_fields = (
        'user__username',
        'user__first_name',
        'user__last_name',
        'user__email',
    )
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_per_page = 20


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_per_page = 20


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'summary',
        'category',
        'published',
        'created_at',
        'updated_at',
    )
    list_filter = ('category', 'published', 'created_at', 'updated_at')
    search_fields = ('title', 'summary', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_per_page = 20


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'post',
        'comment',
        'approved',
        'created_at',
        'updated_at',
    )
    list_filter = ('created_at', 'updated_at')
    search_fields = ('comment', 'name', 'email', 'post__title')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_per_page = 20

    def post(self, obj):
        return obj.post.title
