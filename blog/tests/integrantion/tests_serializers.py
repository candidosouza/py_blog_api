from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import Category, Comment, Post, UserProfile
from blog.serializers import (
    CategorySerializer,
    CommentSerializer,
    ListCommentsPostSerializer,
    ListPostCategorySerializer,
    ListPostsUserSerializer,
    PostSerializer,
)


class CategorySerializerTestCase(TestCase):
    def test_category_serializer(self):
        category = Category.objects.create(
            name='Categoria Teste', slug='categoria-teste'
        )
        serializer = CategorySerializer(category)
        serialized_data = serializer.data

        self.assertEqual(serialized_data['id'], category.id)
        self.assertEqual(serialized_data['name'], 'Categoria Teste')
        self.assertEqual(serialized_data['slug'], 'categoria-teste')
        self.assertEqual(serialized_data['is_active'], True)


class PostSerializerTestCase(TestCase):
    def test_post_serializer(self):
        user = User.objects.create(username='testuser', password='testpass')
        category = Category.objects.create(
            name='Categoria Teste', slug='categoria-teste'
        )
        data = {
            'user': user.id,
            'title': 'Título Teste',
            'slug': 'titulo-teste',
            'summary': 'Resumo teste',
            'content': 'Conteúdo teste',
            'category': category.id,
        }
        serializer = PostSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

        post = serializer.save()
        self.assertEqual(post.title, 'Título Teste')
        self.assertEqual(post.slug, 'titulo-teste')
        self.assertEqual(post.summary, 'Resumo teste')
        self.assertEqual(post.content, 'Conteúdo teste')
        self.assertEqual(post.category, category)
        self.assertEqual(post.published, True)


class CommentSerializerTestCase(TestCase):
    def test_comment_serializer(self):
        user = User.objects.create(username='testuser', password='testpass')
        category = Category.objects.create(
            name='Categoria Teste', slug='categoria-teste'
        )
        post = Post.objects.create(
            user=user,
            title='Título Teste',
            slug='titulo-teste',
            summary='Resumo teste',
            content='Conteúdo teste',
            category=category,
        )
        comment = Comment.objects.create(
            post=post,
            name='John Doe',
            email='johndoe@example.com',
            comment='This is a comment.',
        )
        serializer = CommentSerializer(comment)
        serialized_data = serializer.data

        self.assertEqual(serialized_data['id'], comment.id)
        self.assertEqual(serialized_data['post'], post.id)
        self.assertEqual(serialized_data['name'], 'John Doe')
        self.assertEqual(serialized_data['email'], 'johndoe@example.com')
        self.assertEqual(serialized_data['comment'], 'This is a comment.')
        self.assertEqual(serialized_data['approved'], False)


class ListPostsUserSerializerTestCase(TestCase):
    def test_list_posts_user_serializer(self):
        user = User.objects.create(
            username='testuser',
            password='testpass',
            first_name='John',
            last_name='Doe',
        )
        category = Category.objects.create(
            name='Categoria Teste', slug='categoria-teste'
        )
        post = Post.objects.create(
            user=user,
            title='Título Teste',
            slug='titulo-teste',
            summary='Resumo teste',
            content='Conteúdo teste',
            category=category,
        )
        serializer = ListPostsUserSerializer(post)
        serialized_data = serializer.data

        self.assertEqual(serialized_data['title'], 'Título Teste')
        self.assertEqual(serialized_data['slug'], 'titulo-teste')
        self.assertEqual(serialized_data['summary'], 'Resumo teste')
        self.assertEqual(serialized_data['category'], category.id)
        self.assertEqual(serialized_data['published'], True)
        self.assertEqual(serialized_data['writer'], 'John Doe')


class ListCommentsPostSerializerTestCase(TestCase):
    def test_list_comments_post_serializer(self):
        user = User.objects.create(username='testuser', password='testpass')
        category = Category.objects.create(
            name='Categoria Teste', slug='categoria-teste'
        )
        post = Post.objects.create(
            user=user,
            title='Título Teste',
            slug='titulo-teste',
            summary='Resumo teste',
            content='Conteúdo teste',
            category=category,
        )
        comment = Comment.objects.create(
            post=post,
            name='John Doe',
            email='johndoe@example.com',
            comment='This is a comment.',
        )

        serializer = ListCommentsPostSerializer(comment)
        serialized_data = serializer.data

        self.assertEqual(serialized_data['post'], 'Título Teste')
        self.assertEqual(serialized_data['name'], 'John Doe')
        self.assertEqual(serialized_data['email'], 'johndoe@example.com')
        self.assertEqual(serialized_data['comment'], 'This is a comment.')
        self.assertEqual(serialized_data['approved'], False)


class ListPostCategorySerializerTestCase(TestCase):
    def test_list_post_category_serializer(self):
        user = User.objects.create(username='testuser', password='testpass')
        category = Category.objects.create(
            name='Categoria Teste', slug='categoria-teste'
        )
        post = Post.objects.create(
            user=user,
            title='Título Teste',
            slug='titulo-teste',
            summary='Resumo teste',
            content='Conteúdo teste',
            category=category,
        )
        serializer = ListPostCategorySerializer(post)
        serialized_data = serializer.data

        self.assertEqual(serialized_data['title'], 'Título Teste')
        self.assertEqual(serialized_data['slug'], 'titulo-teste')
        self.assertEqual(serialized_data['summary'], 'Resumo teste')
        self.assertEqual(serialized_data['category'], category.id)
        self.assertEqual(serialized_data['published'], True)
