# -*- coding: utf-8 -*-

# faker to produce fake data
from faker import Factory

# database model
from web.models import Friends

# Django exceptions
from django.core.exceptions import ObjectDoesNotExist

import random

fake = Factory.create()

for x in range(100):
    u = Friends.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        weight=random.randint(40, 150)  # weight : between 40 ~ 150
    )
    u.save()
