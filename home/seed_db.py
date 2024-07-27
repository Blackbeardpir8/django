from home.models import * 
from faker import Faker
import random
fake = Faker('en_IN')

def dbSeeder(records = 10):
    college_names = ['Gec Raipur','Gec Bilaspur','Gec Jagdalpur','VIT','BIT','Rungta','Shankra','KPS']
    for i in college_names:
        address = fake.address()
        College.objects.create(
            college_name = i,
            college_address = address
        )

def dbSeeder2(records = 10):
    colleges = College.objects.all()

    for i in range(records):
        college = random.choice(colleges)
        gender_choice = random.choice(['Male','Female'])
        name = fake.name()
        mobile_mobile = fake.phone_number()
        email = fake.email()
        gender = gender_choice
        age = random.randint(18,26)

        Student.objects.create(
            college = college,
            name = name,
            mobile_mobile = mobile_mobile,
            email = email,
            gender = gender,
            age = age,
        )
