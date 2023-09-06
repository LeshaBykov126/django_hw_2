from django.core.management import BaseCommand
from catalog.models import Category
class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()  # очистка таблицы Category


        new_items = [
            {'name_category': 'Продукты питания', 'category_description': 'Вкусная и полезная еда'},
            {'name_category': 'Электроника', 'category_description': 'Качественная электроника'},
            {'name_category': 'Мебель', 'category_description': 'Удобная мебель'},
        ]

        cat_list = []
        for item_data in new_items:
            cat_list.append(Category(**item_data))

        Category.objects.bulk_create(cat_list)  # заполняем таблицу
