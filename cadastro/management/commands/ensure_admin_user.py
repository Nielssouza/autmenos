import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from decouple import config


class Command(BaseCommand):
    help = "Cria ou atualiza o usuário administrador definido por variáveis de ambiente."

    def handle(self, *args, **options):
        username = config("ADMIN_USERNAME", default=os.getenv("ADMIN_USERNAME", "admin")).strip()
        password = config("ADMIN_PASSWORD", default=os.getenv("ADMIN_PASSWORD", "")).strip()

        if not username:
            self.stdout.write(self.style.WARNING("ADMIN_USERNAME vazio; pulando criação do admin."))
            return

        if not password:
            self.stdout.write(self.style.WARNING("ADMIN_PASSWORD vazio; pulando criação do admin."))
            return

        user_model = get_user_model()
        user, created = user_model.objects.get_or_create(
            username=username,
            defaults={
                "is_staff": True,
                "is_superuser": True,
            },
        )

        changed = created

        if not user.is_staff:
            user.is_staff = True
            changed = True

        if not user.is_superuser:
            user.is_superuser = True
            changed = True

        if not user.check_password(password):
            user.set_password(password)
            changed = True

        if changed:
            user.save()

        if created:
            message = f"Usuário administrador '{username}' criado com sucesso."
        elif changed:
            message = f"Usuário administrador '{username}' atualizado com sucesso."
        else:
            message = f"Usuário administrador '{username}' já está configurado."

        self.stdout.write(self.style.SUCCESS(message))
