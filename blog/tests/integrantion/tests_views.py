from django.contrib.auth.models import User
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.test import APIClient, APITestCase

from blog.models import Category, Comment, Post


class TestBlogViews(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create(username='test', password='test')
        self.user.set_password('test')
        self.user.save()

        self.category = Category.objects.create(
            name='Test Category', slug='test-category'
        )

        self.post = Post.objects.create(
            user=self.user,
            title='Test Title',
            slug='test-slug',
            summary='Test Summary',
            content='Test Content',
            category=self.category,
        )

        self.comment = Comment.objects.create(
            post=self.post,
            name='Test Commenter',
            email='test@gmail.com',
            comment='Test Comment',
        )

    def test_category_list(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_post_list(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_comment_list(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/comments/')
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_list_posts_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f'/api/posts/user/{self.user.id}/')
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_list_post_category(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            f'/api/categories/{self.category.id}/posts/'
        )
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_list_comments_post(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f'/api/posts/{self.post.id}/comments/')
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_unauthenticated_access(self):
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)
