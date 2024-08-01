import os

import django
import itertools
import os

import django.template
os.environ['DJANGO_SETTINGS_MODULE'] = 'firstproject.settings'
django.setup()
import django
import random
from faker import Faker
from home.models import Author, Book, Products, Brand
from datetime import datetime, timedelta
from django.db.models import Sum , Min ,Max,Count,Avg,Q
from home.models import *
fake = Faker()


#def createPerson(number):
#    for i in range (number):
#        Person.objects.create(
#            person_name = fake.name()
#        )

def deletePerson(number):
        Person.objects.all().delete()


deletePerson(10000)


#createPerson(100000)