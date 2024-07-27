from django.shortcuts import render
from django.http import HttpResponse
from home.templates.forms import StudentForm 
from home.models import Student
from django.db.models import Q

def home(request):
    return render(request, 'home.html')

def index(request):
    context = {'form':StudentForm}
    if request.method == "POST":
        data = StudentForm(request.POST)
        if data.is_valid():
           data.save()
        else:
            print(request.method)
    return render(request,"index.html",context)
 
def dynamic_route(request,number):
    for i in range(1,11):
        print(f"{number} X {i} = {number*i}")
    return HttpResponse(f"Response by dynamic route. You Entered {number}")

def renderhtml(request):
    names = ['Deepak','Prashant','Devendra','Shibu','Manish','Milind','Harivansh']
    items = {
        "pen":5,
        "pencil":8,
        "copy":200
    }
    context = {
        "names":names,
        "items":items,
        "fruits":None
    }
    return render(request,'index_i.html',context)

##bakar m bnaya hu 
from faker import Faker
import random

fake = Faker()

def generate_random_person(existing_people):
    while True:
        name = fake.name()
        age = random.randint(0, 100)
        gender = random.choice(['male', 'female'])
        person = {"name": name, "age": age, "gender": gender}
        if person not in existing_people:
            return person

def generate_random_people(n):
    people = []
    for _ in range(n):
        people.append(generate_random_person(people))
    return people


def vote(request):
    people = generate_random_people(10)  
    context = {
        "people": people
    }
    return render(request, 'vote.html', context)

def search_page(request):
    students = Student.objects.all()
 
    search = request.GET.get('search')
    if search:
        students = students.filter(name__icontains=search)

    context = {'students' : students,'search':search }
    return render(request , 'search.html',context)