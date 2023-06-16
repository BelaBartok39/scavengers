import random
from faker import Faker
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from treasure.models import Treasure  # Replace 'myapp' with the name of your app


from django.contrib.auth import get_user_model
User = get_user_model()


fake = Faker()

class Command(BaseCommand):
    help = 'Seed users and treasures'

    def handle(self, *args, **options):
        # Seed 100 user profiles
        for _ in range(100):
            username = fake.user_name()
            password = fake.password()
            email = fake.email()
            User.objects.create_user(username=username, password=password, email=email)

        # Seed 15 treasures per user
        users = User.objects.all()
        treasures = []

        for user in users:
            for _ in range(15):
                name = fake.word()
                description = fake.text()
                longitude = random.uniform(-180, 180)
                latitude = random.uniform(-90, 90)
                hints = fake.text()
                city = fake.city()
                state = fake.state()
                zipcode = fake.zipcode()

                treasure = Treasure(
                    user=user,
                    name=name,
                    description=description,
                    longitude=longitude,
                    latitude=latitude,
                    hints=hints,
                    city=city,
                    state=state,
                    zipcode=zipcode
                )
                treasures.append(treasure)

        Treasure.objects.bulk_create(treasures)

        self.stdout.write(self.style.SUCCESS('Successfully seeded users and treasures.'))
