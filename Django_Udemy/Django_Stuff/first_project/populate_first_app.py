import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

## Fake Pop script
import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','Games','News']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for i in range(N):
        # get topic for the entry
        top = add_topic()
        print(top)
        
        # Create the fake info
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        
        # Create new webpage entry
        webpage = Webpage.objects.create(
            topic = top,
            url = fake_url,
            name = fake_name
        )
        print(webpage)
        webpage.save()
        
        accrec = AccessRecord.objects.create(
            name = webpage,
            date = fake_date
        )
        print(accrec)
        accrec.save()
        
if __name__ == '__main__':
    populate(N=5)
