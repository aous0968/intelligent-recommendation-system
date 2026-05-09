from django.core.management.base import BaseCommand
import pandas as pd
from pathlib import Path
from recommender.models import User , Product, Rating, Behavior

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
users_file = BASE_DIR / 'data_new' / 'users.xlsx'
products_file = BASE_DIR / 'data_new' / 'products.xlsx'
ratings_file = BASE_DIR / 'data_new' / 'ratings.xlsx'
behaviors_file = BASE_DIR / 'data_new' / 'behavior_15500.xlsx'

products = pd.read_excel(products_file)
ratings = pd.read_excel(ratings_file)
behaviors = pd.read_excel(behaviors_file)

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        # users = pd.read_excel(users_file)

        # for _, row in users.iterrows():

        #     User.objects.get_or_create(
        #         user_id=row['user_id'],
        #         defaults={
        #             'age': row['age'],
        #             'country': row['country']
        #         }
        #     )

        # self.stdout.write(self.style.SUCCESS('Users imported'))


        for _, row in products.iterrows():

            Product.objects.get_or_create(
                product_id=row['product_id'],
                defaults={
                    'category': row['category'],
                    'price': row['price']
                }
            )

        self.stdout.write(self.style.SUCCESS('Products imported'))

        for _, row in ratings.iterrows():

            try:
                user = User.objects.get(user_id=row['user_id'])
                product = Product.objects.get(product_id=row['product_id'])

                Rating.objects.get_or_create(
                    user=user,
                    product=product,
                    defaults={
                        'rating': row['rating']
                    }
                )

            except:
                pass

        self.stdout.write(self.style.SUCCESS('Ratings imported'))

        for _, row in behaviors.iterrows():

            try:

                user = User.objects.get(user_id=row['user_id'])
                product = Product.objects.get(product_id=row['product_id'])

                Behavior.objects.get_or_create(
                    user=user,
                    product=product,
                    defaults={
                        'viewed': row['viewed'],
                        'clicked': row['clicked'],
                        'purchased': row['purchased']
                    }
                )

            except:
                pass

        self.stdout.write(self.style.SUCCESS('Behavior imported'))