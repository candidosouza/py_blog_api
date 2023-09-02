from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models

CREATED_AT = 'Criado em'
UPDATED_AT = 'Atualizado em'


class UserProfile(models.Model):
    TYPE = (
        ('A', 'Admin'),
        ('M', 'Moderator'),
        ('E', 'Escritor'),
    )
    user = models.OneToOneField(
        User,
        unique=True,
        on_delete=models.CASCADE,
        related_name='user_profile',
        verbose_name='Usuário',
    )
    type_user = models.CharField(
        max_length=1, choices=TYPE, default='E', verbose_name='Tipo de Usuário'
    )
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    last_seen = models.DateTimeField(
        null=True, blank=True, verbose_name='Último acesso'
    )
    biography = models.TextField(
        blank=True, unique=True, verbose_name='Biografia'
    )
    facebook = models.CharField(
        max_length=100, blank=True, unique=True, verbose_name='Facebook'
    )
    linkedin = models.CharField(
        max_length=100, blank=True, unique=True, verbose_name='Linkedin'
    )
    instagram = models.CharField(
        max_length=100, blank=True, unique=True, verbose_name='Instagram'
    )
    twitter = models.CharField(
        max_length=100, blank=True, unique=True, verbose_name='Twitter'
    )
    github = models.CharField(
        max_length=100, blank=True, unique=True, verbose_name='Github'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=CREATED_AT
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=UPDATED_AT)

    class Meta:
        db_table = 'user_profiles'
        verbose_name = 'Perfil do Usuário'
        verbose_name_plural = 'Perfis dos Usuários'

    def __str__(self):
        return f'Perfil: {self.user.first_name} {self.user.last_name}'


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Nome',
        validators=[MinLengthValidator(3), MaxLengthValidator(100)],
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name='Slug',
        validators=[MinLengthValidator(3), MaxLengthValidator(100)],
    )
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=CREATED_AT
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=UPDATED_AT)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created_at',)
        db_table = 'category'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Título',
        validators=[MinLengthValidator(3), MaxLengthValidator(100)],
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name='Slug',
        validators=[MinLengthValidator(3), MaxLengthValidator(100)],
    )
    summary = models.CharField(
        max_length=200,
        verbose_name='Resumo',
        validators=[MinLengthValidator(3), MaxLengthValidator(200)],
    )
    content = models.TextField(verbose_name='Conteúdo')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Categoria'
    )
    published = models.BooleanField(default=True, verbose_name='Publicado')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=CREATED_AT
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=UPDATED_AT)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)
        db_table = 'post'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=100,
        verbose_name='Nome',
        validators=[MinLengthValidator(3), MaxLengthValidator(100)],
    )
    email = models.EmailField(verbose_name='E-mail')
    comment = models.TextField(verbose_name='Comentário')
    approved = models.BooleanField(default=False, verbose_name='Aprovado')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=CREATED_AT
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=UPDATED_AT)

    class Meta:
        ordering = ('created_at',)
        db_table = 'comment'
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    def __str__(self):
        return f'Comentado por {self.name} em {self.post.title}'
