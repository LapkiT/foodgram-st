import json
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from recipes.models import Ingredient

class Command(BaseCommand):
    help = 'Загружает ингредиенты из <filename>.json в /app/fixtures/ в базу данных'
    FIXTURES_DIR = Path('/app/fixtures')

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='Имя файла (например, ingredients.json) в директории /app/fixtures/')
        parser.add_argument('--clear', action='store_true', help='Очистить таблицу Ingredient перед загрузкой новых данных.')

    def handle(self, *args, **options):
        filename = options['filename']
        clear_table = options['clear']
        file_path = self.FIXTURES_DIR / filename
        try:
            if clear_table:
                Ingredient.objects.all().delete()
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            if not isinstance(data, list):
                raise CommandError('JSON файл должен содержать список объектов.')
            existing = set(Ingredient.objects.values_list('name', flat=True))
            to_create = [Ingredient(**item) for item in data if isinstance(item, dict) and item.get('name') and item.get('measurement_unit') and item['name'].lower() not in existing]
            for item in to_create:
                existing.add(item.name.lower())
            created = Ingredient.objects.bulk_create(to_create, ignore_conflicts=True)
            summary = (
                f'Загрузка из "{filename}" завершена. '
                f'Добавлено новых: {len(created)}, '
                f'Пропущено/Обновлено: {len(data) - len(created)}, '
                f'Ошибок при сохранении: 0.'
            )
            self.stdout.write(self.style.SUCCESS(summary))
        except Exception as e:
            raise CommandError(f'Ошибка загрузки из "{filename}": {e}')
