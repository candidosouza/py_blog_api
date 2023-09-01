import random

from django.contrib.auth.models import User
from django.utils import timezone
from faker import Faker

from blog.models import Category, Post, UserProfile, Comment

User.objects.all().delete()
UserProfile.objects.all().delete()
Category.objects.all().delete()
Post.objects.all().delete()

# create superuser
User.objects.create_superuser(
    username='admin', email='admin@email.com', password='admin'
)

fake = Faker('pt_BR')

# Cria usuários
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

# Cria categorias
for _ in range(5):
    name = fake.word()
    Category.objects.create(
        name=name, slug=name.lower(), is_active=random.choice([True, False])
    )

# Cria posts
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

# Cria Comentários
for _ in range(50):
    post = random.choice(Post.objects.all())
    Comment.objects.create(
        name=f'{fake.first_name()} {fake.last_name()}',
        email=fake.email(),
        post=post,
        comment=fake.text(),
        approved=random.choice([True, False]),
    )

