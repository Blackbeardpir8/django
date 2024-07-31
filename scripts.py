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
from django.db.models import Sum , Min ,Max,Count,Avg


def handle():
    #authors = Author.objects.annotate(total_books = Count('book'))
    authors = Author.objects.annotate(avg_price = Avg('book__price'),total_books = Count('book'))
    
    for author in authors:
        print(f"Author name {author.author_name} total book {author.total_books} total avg price {author.avg_price}")
    

handle()