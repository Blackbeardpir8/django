from django import forms
from home.models import Student

class StudentForm(forms.ModelForm):
   class Meta:
      model = Student
      fields = '__all__' # for all fields
      #fields = ['name','gender.]   # for specific fields