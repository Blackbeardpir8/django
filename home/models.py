from django.db import models


# Create your models here.
class College(models.Model):
    college_name = models.CharField(max_length=100)
    college_address = models.CharField(max_length=100)

class Student(models.Model):
    gender_choices = (('Male','Male'),('Female','Female'))
    name = models.CharField(max_length=50)
    mobile_mobile = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10,choices=gender_choices, default="Male")
    age = models.IntegerField(null=True,blank=True)
    college = models.ForeignKey(College,on_delete=models.CASCADE,null=True,blank=True)
    

## Oneto one relationship
class Author(models.Model):
    author_name = models.CharField(max_length=100)


class Book(models.Model): 
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100)

## Foreign Key or One to Many relationship
class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    country = models.CharField(default="India",max_length=100)   
    
    def __str__(self) -> str:
        return self.brand_name

class Products(models.Model):
     brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
     prduct_name = models.CharField(max_length=100)

## many to many relationship
class Skills(models.Model):
    skill_name = models.CharField(max_length=100)
    
class Person(models.Model):
    person_name = models.CharField(max_length=100)
    skill = models.ManyToManyField(Skills)


## for inserting data from front end to database()

class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


