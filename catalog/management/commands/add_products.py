from django.core.management.base import BaseCommand
from django.core.management import call_command

from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Добавляет тестовые данные для продуктов и категорий"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()
        call_command("loaddata", "categories_fixture.json")
        call_command("loaddata", "products_fixture.json")
        self.stdout.write(self.style.SUCCESS("Успешно загружены данные из фикстуры"))
