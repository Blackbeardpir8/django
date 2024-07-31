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
from django.db.models import Sum , Min ,Max,Count,Avg,Q


def handle():
    authors = Author.objects.annotate(
       total_earning=Sum('book__price'),
       book_count_2023 = Count('book' , filter=Q(book__published_date__year = 2023))
        )
    
    for author in authors:
        print(f"Author name = {author.author_name}, earning = {author.total_earning} Book Count {author.book_count_2023} ")

handle()
