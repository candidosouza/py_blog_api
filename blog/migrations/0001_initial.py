# Generated by Django 4.2.5 on 2023-09-06 13:14

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(100)], verbose_name='Nome')),
                ('slug', models.SlugField(max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(100)], verbose_name='Slug')),
                ('image', models.ImageField(blank=True, null=True, upload_to='category', verbose_name='Imagem')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'category',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_user', models.CharField(choices=[('A', 'Admin'), ('M', 'Moderator'), ('E', 'Escritor')], default='E', max_length=1, verbose_name='Tipo de Usuário')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('last_seen', models.DateTimeField(blank=True, null=True, verbose_name='Último acesso')),
                ('biography', models.TextField(blank=True, unique=True, verbose_name='Biografia')),
                ('facebook', models.CharField(blank=True, max_length=100, unique=True, verbose_name='Facebook')),
                ('linkedin', models.CharField(blank=True, max_length=100, unique=True, verbose_name='Linkedin')),
                ('instagram', models.CharField(blank=True, max_length=100, unique=True, verbose_name='Instagram')),
                ('twitter', models.CharField(blank=True, max_length=100, unique=True, verbose_name='Twitter')),
                ('github', models.CharField(blank=True, max_length=100, unique=True, verbose_name='Github')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Perfil do Usuário',
                'verbose_name_plural': 'Perfis dos Usuários',
                'db_table': 'user_profiles',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(100)], verbose_name='Título')),
                ('slug', models.SlugField(max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(100)], verbose_name='Slug')),
                ('summary', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(200)], verbose_name='Resumo')),
                ('content', models.TextField(verbose_name='Conteúdo')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts', verbose_name='Imagem')),
                ('published', models.BooleanField(default=True, verbose_name='Publicado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category', verbose_name='Categoria')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'db_table': 'post',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(100)], verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('comment', models.TextField(verbose_name='Comentário')),
                ('approved', models.BooleanField(default=False, verbose_name='Aprovado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
            options={
                'verbose_name': 'Comentário',
                'verbose_name_plural': 'Comentários',
                'db_table': 'comment',
                'ordering': ('created_at',),
            },
        ),
    ]
