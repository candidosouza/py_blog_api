from unittest import TestCase

from django.contrib.auth.models import User
from django.utils.dateparse import parse_datetime
from rest_framework.exceptions import ValidationError

from blog.models import Category, Post
from blog.serializers import CategorySerializer, PostSerializer


class TestCategorySerializer(TestCase):
    def test_valid_serializer(self):
        category = Category(name='Tech', slug='tech')
        category.save()

        serializer = CategorySerializer(instance=category)

        serializer_data = serializer.data
        serializer_data['created_at'] = parse_datetime(
            serializer_data['created_at']
        )
        serializer_data['updated_at'] = parse_datetime(
            serializer_data['updated_at']
        )

        self.assertEqual(
            serializer_data,
            {
                'id': category.id,
                'name': 'Tech',
                'slug': 'tech',
                'is_active': True,
                'created_at': category.created_at,
                'updated_at': category.updated_at,
            },
        )

        self.assertEqual(serializer.data['name'], 'Tech')
        self.assertEqual(serializer.data['slug'], 'tech')

    def test_invalid_serializer(self):
        data = {'name': '', 'slug': 'tech'}

        serializer = CategorySerializer(data=data)

        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)


# TODO: testar os demais serializers
