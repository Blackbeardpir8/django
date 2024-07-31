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
        book_count = Count('book',filter =Q(book__price__gte = 50))
        )
    for author in authors:
        print(f"Author name = {author.author_name} Book count {author.book_count}")

handle()