from django.shortcuts import render
from app1.forms import Student
from app1.models import Students

# Create your views here.
def student(request):
    form=Student()
    if request.method =='POST':
        form=Student(request.POST)
        form.is_valid()
        name = form.cleaned_data['name'].upper()
        email= form.cleaned_data['email']
        courses= form.cleaned_data['courses']
        jdate=form.cleaned_data['jdate']
        stud=Students(name=name,email=email,courses=courses,jdate=jdate)
        stud.save()
    else:
        print("invalid data")
    form=Student()
    return render(request,'app1/student.html',{'form':form})
