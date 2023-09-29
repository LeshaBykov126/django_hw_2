from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):


    def handle(self, *args, **options):
        self.stdout.write("Clearing old data from the database...")
        Category.objects.all().delete()  # очистка таблицы Category
        Product.objects.all().delete()  # очистка таблицы Product

        self.stdout.write("Populating database with new data...")

        category1 = Category.objects.create(name='Category 1')
        category2 = Category.objects.create(name='Category 2')

        Product.objects.create(name='Product 1', category=category1, unit_price=10)
        Product.objects.create(name='Product 2', category=category2, unit_price=20)

        self.stdout.write(self.style.SUCCESS("Database has been populated successfully"))
        # new_items = [
        #     {'name_category': 'Продукты питания', 'category_description': 'Вкусная и полезная еда'},
        #     {'name_category': 'Электроника', 'category_description': 'Качественная электроника'},
        #     {'name_category': 'Мебель', 'category_description': 'Удобная мебель'},
        # ]
        #
        # cat_list = []
        # for item_data in new_items:
        #     cat_list.append(Category(**item_data))
        #
        # Category.objects.bulk_create(cat_list)  # заполняем таблицу
