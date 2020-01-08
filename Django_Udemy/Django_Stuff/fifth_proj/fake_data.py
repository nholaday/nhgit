import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fifth_proj.settings')

import django
django.setup()
from users_app.models import User
from faker import Faker
from pprint import pprint

def pop_user():
    """Creates User object with fake data"""
    u = User.objects.create()
    fake = Faker()
    u.firstname = fake.first_name()
    u.lastname = fake.last_name()
    u.email = fake.email()

    pprint(vars(u))
    u.save()


if __name__ == "__main__":
    for i in range(10):
        pop_user()
