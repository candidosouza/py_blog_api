import random

from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.core.management import call_command
from django.utils import timezone
from faker import Faker

from blog.models import Category, Comment, Post, UserProfile

# Flush the database
call_command('flush', interactive=False)

# Iniciar Faker
fake = Faker('pt_BR')

# 1. Criar superusuário
User.objects.create_superuser(
    username='admin',
    email='admin@email.com',
    password='admin',
    first_name='Admin',
    last_name='Admin',
)

# 2. Criar usuários e seus perfis
for _ in range(10):
    username = fake.user_name()
    email = fake.email()
    user = User.objects.create_user(
        username=username,
        email=email,
        password='123456',
        first_name=fake.first_name(),
        last_name=fake.last_name(),
    )

    UserProfile.objects.create(
        user=user,
        type_user=random.choice(['A', 'M', 'E']),
        is_active=random.choice([True, False]),
        last_seen=timezone.now(),
        biography=fake.text(),
        facebook=fake.user_name(),
        linkedin=fake.user_name(),
        instagram=fake.user_name(),
        twitter=fake.user_name(),
        github=fake.user_name(),
    )

# 3. Criar categorias
for _ in range(5):
    name = fake.word()
    Category.objects.create(
        name=name, slug=name.lower(), is_active=random.choice([True, False])
    )

# 4. Criar posts
for _ in range(20):
    title = fake.sentence()
    user = random.choice(User.objects.filter(user_profile__type_user='E'))
    category = random.choice(Category.objects.all())
    Post.objects.create(
        user=user,
        title=title,
        slug=title.lower().replace(' ', '-'),
        summary=fake.sentence(),
        content=fake.text(),
        category=category,
        published=random.choice([True, False]),
    )

# 5. Criar comentários
for _ in range(50):
    post = random.choice(Post.objects.all())
    Comment.objects.create(
        name=f'{fake.first_name()} {fake.last_name()}',
        email=fake.email(),
        post=post,
        comment=fake.text(),
        approved=random.choice([True, False]),
    )

content_type = ContentType.objects.get_for_model(Post)
post_permissions = Permission.objects.filter(content_type=content_type)
filtered_permissions = [
    p for p in post_permissions if p.codename != 'delete_post'
]

# for permission in filtered_permissions:
#     print(permission.codename)

for user in User.objects.filter(user_profile__type_user='E'):
    user.user_permissions.add(*filtered_permissions)
