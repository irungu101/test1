from django.shortcuts import render,redirect
from Registration.forms import EmployeeForm
from Registration.models import Student
from Registration.forms import StudentForm



def application_form(request):
    form = EmployeeForm()
    return render(request, 'application.html', {'form':form})

def application_list(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = StudentForm()
        else:
            employee = Student.objects.get(pk=id)
            form = StudentForm(instance=employee)
        return render(request, 'application_list.html', {'form':form})
    else:
        if id == 0:
            form = StudentForm(request.POST)
        else:
            employee = Student.objects.get(pk=id)
            form = StudentForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/Registration/show')


def show(request):
    context = {'show': Student.objects.all()}
    return render(request, 'show.html', context)