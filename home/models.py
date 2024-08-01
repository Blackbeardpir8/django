from typing import Iterable
from django.db import models
from django.template.defaultfilters import slugify
from home.utils import generateSlug


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
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)  # Allowing null
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Setting a default value

    class Meta:
        db_table = "book"
        ordering = ('-price',)
        verbose_name = "Book"
        verbose_name_plural = "Book"

## Foreign Key or One to Many relationship
class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    country = models.CharField(default="India",max_length=100)   
    
    def __str__(self) -> str:
        return self.brand_name
    
    class Meta:
        unique_together = ('brand_name', 'country')
        index_together = ('brand_name', 'country')


class Products(models.Model):
     brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
     prduct_name = models.CharField(max_length=100)
     slug = models.SlugField(max_length=100 ,null=True,blank=True)

     def save(self, *args , **kwargs) -> None:
         if not self.id:
             self.slug = generateSlug(self.prduct_name,Products)

         return super().save(*args, **kwargs)

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


class Human(models.Model):
    name = models.CharField(max_length=100)
    age =models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Engineer(Human):
    technology = models.CharField(max_length=100)

class HR(Human):
    responsibility = models.CharField(max_length=100)

class Investor(Human):
    money = models.CharField(max_length=100)