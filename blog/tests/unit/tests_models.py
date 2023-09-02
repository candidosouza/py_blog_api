from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import Category, Comment, Post, UserProfile


class UserProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser', password='testpass'
        )
        self.user_profile = UserProfile.objects.create(
            user=self.user, type_user='A'
        )

    def test_user_profile_creation(self):
        self.assertEqual(
            str(self.user_profile),
            f'Perfil: {self.user.first_name} {self.user.last_name}',
        )


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='TestCategory', slug='test-category'
        )

    def test_category_creation(self):
        self.assertEqual(str(self.category), 'TestCategory')


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser', password='testpass'
        )
        self.category = Category.objects.create(
            name='TestCategory', slug='test-category'
        )
        self.post = Post.objects.create(
            user=self.user,
            title='TestTitle',
            slug='test-title',
            summary='TestSummary',
            content='TestContent',
            category=self.category,
        )

    def test_post_creation(self):
        self.assertEqual(str(self.post), 'TestTitle')


class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser', password='testpass'
        )
        self.category = Category.objects.create(
            name='TestCategory', slug='test-category'
        )
        self.post = Post.objects.create(
            user=self.user,
            title='TestTitle',
            slug='test-title',
            summary='TestSummary',
            content='TestContent',
            category=self.category,
        )
        self.comment = Comment.objects.create(
            post=self.post,
            name='TestName',
            email='test@example.com',
            comment='TestComment',
        )

    def test_comment_creation(self):
        self.assertEqual(
            str(self.comment), 'Comentado por TestName em TestTitle'
        )
