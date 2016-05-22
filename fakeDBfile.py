# -*- coding: utf-8 -*-

# faker to produce fake data
from faker import Factory

# database model
from web.models import User

# Django exceptions
from django.core.exceptions import ObjectDoesNotExist

import random

fake = Factory.create()

for x in range(100):
    u = User.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        weight=random.randint(40, 150)
    )
    u.save()