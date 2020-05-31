from django.shortcuts import render, redirect
from .models import Tools, Rental, Employee
from .forms import ToolForm, EmployeeForm, RentalForm

# Create your views here.
def new_tool(request):
    form_tool = ToolForm(request.POST or None, request.FILES or None)

    if form_tool.is_valid():
        form_tool.save()
        return redirect(tools_list)

    context = {
        'form_tool': form_tool
    }

    return render(request, 'forms/form_tools.html', context)


def tools_list(request):
    tools = Tools.objects.all().order_by('name')

    context = {
        'tools': tools
    }
    return render(request,'forms/tools.html',context)


def new_employee(request):
    form_employee = EmployeeForm(request.POST or None, request.FILES or None)

    if form_employee.is_valid():
        form_employee.save()
        return redirect(employee_list)

    context = {
        'form_employee': form_employee
    }

    return render(request, 'forms/form_employee.html', context)


def employee_list(request):
    employee = Employee.objects.all().order_by('name')

    context = {
        'employee': employee
    }
    return render(request,'forms/employee.html',context)


def new_rental(request):
    form_rental = RentalForm(request.POST or None, request.FILES or None)

    if form_rental.is_valid():
        form_rental.save()
        return redirect(rental_list)

    context = {
        'form_rental': form_rental
    }

    return render(request, 'forms/form_rental.html', context)


def rental_list(request):
    rental = Rental.objects.all().order_by('tools')

    context = {
        'rental': rental
    }
    return render(request,'forms/rental.html',context)

