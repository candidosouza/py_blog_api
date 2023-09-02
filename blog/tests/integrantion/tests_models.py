from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import Category, Comment, Post, UserProfile


class ModelsIntegrationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser', password='testpass'
        )
        self.user_profile = UserProfile.objects.create(
            user=self.user, type_user='A'
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

    def test_create_comment_on_post(self):
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.name, 'TestName')
        self.assertEqual(self.comment.email, 'test@example.com')

    def test_create_post_in_category(self):
        self.assertEqual(self.post.category, self.category)
        self.assertEqual(self.post.title, 'TestTitle')

    def test_user_profile(self):
        self.assertEqual(self.user_profile.user, self.user)
        self.assertEqual(self.user_profile.type_user, 'A')

    def test_post_by_user(self):
        self.assertEqual(self.post.user, self.user)
        self.assertEqual(self.post.title, 'TestTitle')

    def test_comment_approved_default(self):
        self.assertFalse(self.comment.approved)

    def test_user_profile_association(self):
        self.assertEqual(self.user_profile.user, self.post.user)
