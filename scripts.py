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
       total_earning=Sum('book__price',)
    )
    
    for author in authors:
        print(f"Author name = {author.author_name}, earning = {author.total_earning}")

handle()
