from unittest.mock import Mock

from django.contrib.admin.sites import AdminSite
from django.test import TestCase

from blog.admin import CategoryAdmin, CommentAdmin, PostAdmin, UserProfileAdmin
from blog.models import Category, Comment, Post, UserProfile


class MockRequest:
    pass


request = MockRequest()


class UserProfileAdminTestCase(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin = UserProfileAdmin(UserProfile, self.site)

    def test_list_display(self):
        self.assertEqual(
            list(self.admin.list_display),
            [
                'user',
                'type_user',
                'is_active',
                'last_seen',
                'created_at',
                'updated_at',
            ],
        )


class CategoryAdminTestCase(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin = CategoryAdmin(Category, self.site)

    def test_list_display(self):
        self.assertEqual(
            list(self.admin.list_display),
            ['name', 'slug', 'is_active', 'created_at', 'updated_at'],
        )


class PostAdminTestCase(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin = PostAdmin(Post, self.site)

    def test_list_display(self):
        self.assertEqual(
            list(self.admin.list_display),
            [
                'title',
                'slug',
                'summary',
                'category',
                'published',
                'created_at',
                'updated_at',
            ],
        )


class CommentAdminTestCase(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin = CommentAdmin(Comment, self.site)

    def test_list_display(self):
        self.assertEqual(
            list(self.admin.list_display),
            [
                'name',
                'email',
                'post',
                'comment',
                'approved',
                'created_at',
                'updated_at',
            ],
        )
