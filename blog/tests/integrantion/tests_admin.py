from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import Category, Comment, Post, UserProfile


class AdminIntegrationTest(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            'admin', 'admin@example.com', 'password123'
        )
        self.client.login(username='admin', password='password123')
        self.profile = UserProfile.objects.create(
            user=self.admin_user, type_user='A'
        )
        self.category = Category.objects.create(
            name='Tech', slug='tech', image=''
        )
        self.post = Post.objects.create(
            user=self.admin_user,
            title='Test Post',
            slug='test-post',
            summary='Summary',
            content='Here is some content.',
            category=self.category,
        )
        self.comment = Comment.objects.create(
            post=self.post,
            name='Commenter',
            email='commenter@example.com',
            comment='Great post!',
        )

    def test_category_admin_page(self):
        response = self.client.get('/admin/blog/category/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Selecione Categoria para modificar')

    def test_post_admin_page(self):
        response = self.client.get('/admin/blog/post/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Selecione Post para modificar')

    def test_comment_admin_page(self):
        response = self.client.get('/admin/blog/comment/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Selecione Comentário para modificar')
