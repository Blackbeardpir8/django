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



Products.objects.create(brand = Brand.objects.first(),
                        prduct_name = "trimmer men with perfect trim"
                        )