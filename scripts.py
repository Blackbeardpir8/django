import os

import django
import itertools
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'firstproject.settings'
django.setup()
import django
import random
from faker import Faker
from home.models import Author, Book
from datetime import datetime, timedelta
from django.db.models import Sum 


def handle():
    #books = Book.objects.Sum()
    #books = Book.objects.aggregate(price = Avg('price'))
    books = Book.objects.aggregate(price = Sum('price'))
    print(books)

handle()