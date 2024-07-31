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
from django.db.models import Sum , Min ,Max,Count


def handle():
    authors = Author.objects.annotate(total_books = Count('book'))

    for author in authors:
        print("Author name {author.author_name} total books{author.total_books}")
    print(authors)

handle()