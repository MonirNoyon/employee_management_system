
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})


def update_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/update_employee.html', {'form': form})

def delete_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('home')
    return render(request, 'employees/delete_employee.html', {'employee': employee})

def home(request):
    employees = Employee.objects.all()
    return render(request, 'employees/home.html', {'employees': employees})