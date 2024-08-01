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


def createPerson(number):
    create = [Person(person_name = fake.name()) for i in range (number)]
    Person.objects.bulk_create(create)


    
#def deletePerson(number):
#        Person.objects.all.delete()#

#deletePerson(1000)


createPerson(100000)