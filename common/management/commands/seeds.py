from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from blog.models import Category, Post, UserProfile


class Command(BaseCommand):
    help = 'Seed database with initial data'

    def handle(
        self, *args, **kwargs
    ):  # sourcery skip: remove-unreachable-code
        try:
            self.stdout.write('Deleting existing data...')
            # Limpa os dados existentes
            User.objects.all().delete()
            UserProfile.objects.all().delete()
            Category.objects.all().delete()
            Post.objects.all().delete()
            # Adicione outras chamadas de deletar para outros apps

            self.stdout.write('Seeding data...')

            # Chamar diferentes scripts de seed para cada app
            exec(open('blog/fixtures/seeds.py').read())
            # Adicione outras chamadas de seed para outros apps

            self.stdout.write('Data seeded successfully.')
        except Exception as e:
            raise e
            self.stderr.write(f'Error seeding data: {e}')
