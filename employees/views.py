from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EmployeeForm
from .models import Department, Employee


@login_required
def employee_list(request):
    employees = Employee.objects.select_related('department').all()

    search = request.GET.get('search', '').strip()
    department_id = request.GET.get('department', '').strip()
    employee_name = request.GET.get('employee_name', '').strip()
    employee_id = request.GET.get('employee_id', '').strip()

    if search:
        employees = employees.filter(
            Q(employee_id__icontains=search) |
            Q(name__icontains=search)
        )

    if department_id:
        employees = employees.filter(department_id=department_id)

    if employee_name:
        employees = employees.filter(id=employee_name)

    if employee_id:
        employees = employees.filter(employee_id=employee_id)

    departments = Department.objects.all().order_by('name')
    employee_options = Employee.objects.all().order_by('name')

    return render(
        request,
        'employees/employee_list.html',
        {
            'employees': employees,
            'departments': departments,
            'employee_options': employee_options,
            'search': search,
            'selected_department': department_id,
            'selected_employee_name': employee_name,
            'selected_employee_id': employee_id,
        }
    )


@login_required
def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Employee added successfully.')
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(
        request,
        'employees/employee_form.html',
        {
            'form': form,
            'title': 'Add Employee',
        }
    )


@login_required
def employee_edit(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            messages.success(request, 'Employee updated successfully.')
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)

    return render(
        request,
        'employees/employee_form.html',
        {
            'form': form,
            'title': 'Edit Employee',
        }
    )


@login_required
def employee_delete(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employee deleted successfully.')
        return redirect('employee_list')

    return render(
        request,
        'employees/employee_confirm_delete.html',
        {
            'employee': employee,
        }
    )


@login_required
def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    return render(
        request,
        'employees/employee_detail.html',
        {
            'employee': employee,
        }
    )