from django.contrib.auth.models import User
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
)
from rest_framework.test import APIClient, APITestCase

from blog.models import Category, Comment, Post, UserProfile


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

    def test_category_create(self):
        user = User.objects.create_superuser(
            'myuser_unique', 'myemail_unique@test.com', 'teste'
        )
        self.client.force_authenticate(user=user)
        response = self.client.post(
            '/api/categories/?format=json',
            {
                'name': 'Test Category Unique',
                'slug': 'test-category-unique',
                'image': '',
                'is_active': True,
            },
        )
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_post_create(self):
        user = User.objects.create_superuser(
            'myuser_unique', 'myemail_unique@test.com', 'teste'
        )
        self.client.force_authenticate(user=user)
        response = self.client.post(
            '/api/posts/',
            {
                'user': self.user.id,
                'title': 'Test Title Unique',
                'slug': 'test-slug-unique',
                'summary': 'Test Summary',
                'content': 'Test Content',
                'category': self.category.id,
                'image': '',
                'published': True,
            },
        )
        if response.status_code != HTTP_201_CREATED:
            print(response.data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_comment_create(self):
        user = User.objects.create_superuser(
            'myuser_unique', 'myemail_unique@test.com', 'teste'
        )
        self.client.force_authenticate(user=user)
        response = self.client.post(
            '/api/comments/',
            {
                'post': self.post.id,
                'name': 'Test Commenter',
                'email': 'myemail_unique@test.com',
                'comment': 'Test Comment',
                'approved': True,
            },
        )
        if response.status_code != HTTP_201_CREATED:
            print(response.data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_category_updated(self):
        user = User.objects.create_superuser(
            'myuser_unique', 'myemail_unique@test.com', 'teste'
        )
        self.client.force_authenticate(user=user)
        response = self.client.put(
            f'/api/categories/{self.category.id}/',
            {
                'name': 'Test Category Unique',
                'slug': 'test-category-unique',
                'image': '',
                'is_active': True,
            },
        )
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_post_updated(self):
        user = User.objects.create_superuser(
            'myuser_unique', 'myemail_unique@test.com', 'teste'
        )
        self.client.force_authenticate(user=user)
        response = self.client.put(
            f'/api/posts/{self.post.id}/',
            {
                'user': self.user.id,
                'title': 'Test Title Unique',
                'slug': 'test-slug-unique',
                'summary': 'Test Summary',
                'content': 'Test Content',
                'category': self.category.id,
                'image': '',
                'published': True,
            },
        )
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_comment_updated(self):
        user = User.objects.create_superuser(
            'myuser_unique', 'myemail_unique@test.com', 'teste'
        )
        self.client.force_authenticate(user=user)
        response = self.client.put(
            f'/api/comments/{self.comment.id}/',
            {
                'post': self.post.id,
                'name': 'Test Commenter',
                'email': 'test@email.com',
                'comment': 'Test Comment Updated',
                'approved': True,
            },
        )
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_category_delete(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/api/categories/{self.category.id}/')
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_post_delete(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/api/posts/{self.post.id}/')
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_comment_delete(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/api/comments/{self.comment.id}/')
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)
