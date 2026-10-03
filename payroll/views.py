from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from calendar import monthrange
from datetime import date
from attendance.models import Attendance, Leave

from .forms import PayrollForm
from .models import Payroll

@login_required
def dashboard(request):
    from employees.models import Employee
    from attendance.models import Attendance, Leave
    from .models import Payroll

    total_employees = Employee.objects.count()
    total_payrolls = Payroll.objects.count()
    total_attendance = Attendance.objects.count()
    total_leaves = Leave.objects.count()

    total_salary = sum(
        payroll.net_salary
        for payroll in Payroll.objects.all()
    )

    context = {
        'total_employees': total_employees,
        'total_payrolls': total_payrolls,
        'total_attendance': total_attendance,
        'total_leaves': total_leaves,
        'total_salary': total_salary,
    }

    return render(request, 'dashboard.html', context)


@login_required
def payroll_list(request):
    payrolls = Payroll.objects.select_related('employee').all()

    return render(request, 'payroll/payroll_list.html', {
        'payrolls': payrolls
    })


@login_required
def payroll_add(request):
    if request.method == 'POST':
        form = PayrollForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Payroll record added successfully.'
            )
            return redirect('payroll_list')

    else:
        form = PayrollForm()

    return render(request, 'payroll/payroll_form.html', {
        'form': form,
        'title': 'Add Payroll'
    })


@login_required
def payroll_edit(request, payroll_id):
    payroll = get_object_or_404(Payroll, id=payroll_id)

    if request.method == 'POST':
        form = PayrollForm(request.POST, instance=payroll)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Payroll record updated successfully.'
            )
            return redirect('payroll_list')

    else:
        form = PayrollForm(instance=payroll)

    return render(request, 'payroll/payroll_form.html', {
        'form': form,
        'title': 'Edit Payroll'
    })


@login_required
def payroll_delete(request, payroll_id):
    payroll = get_object_or_404(Payroll, id=payroll_id)

    if request.method == 'POST':
        payroll.delete()
        messages.success(
            request,
            'Payroll record deleted successfully.'
        )
        return redirect('payroll_list')

    return render(request, 'payroll/payroll_confirm_delete.html', {
        'payroll': payroll
    })

@login_required
def salary_slip(request, payroll_id):
    payroll = get_object_or_404(
        Payroll.objects.select_related('employee'),
        id=payroll_id
    )

    return render(request, 'payroll/salary_slip.html', {
        'payroll': payroll
    })

@login_required
def attendance_salary(request, payroll_id):
    payroll = get_object_or_404(
        Payroll.objects.select_related('employee'),
        id=payroll_id
    )

    employee = payroll.employee

    year = payroll.month.year
    month = payroll.month.month

    total_days = monthrange(year, month)[1]

    attendance_records = Attendance.objects.filter(
        employee=employee,
        date__year=year,
        date__month=month
    )

    present_days = attendance_records.filter(
        status='Present'
    ).count()

    absent_days = attendance_records.filter(
        status='Absent'
    ).count()

    leave_days = attendance_records.filter(
        status='Leave'
    ).count()

    daily_salary = payroll.basic_salary / total_days

    paid_days = present_days + leave_days

    attendance_salary_amount = daily_salary * paid_days

    final_salary = (
        attendance_salary_amount
        + payroll.allowances
        - payroll.deductions
    )

    return render(request, 'payroll/attendance_salary.html', {
        'payroll': payroll,
        'total_days': total_days,
        'present_days': present_days,
        'absent_days': absent_days,
        'leave_days': leave_days,
        'paid_days': paid_days,
        'daily_salary': daily_salary,
        'attendance_salary_amount': attendance_salary_amount,
        'final_salary': final_salary,
    })

@login_required
def payroll_report(request):

    payrolls = Payroll.objects.select_related('employee').all()

    employee_id = request.GET.get('employee')
    selected_month = request.GET.get('month')

    if employee_id:
        payrolls = payrolls.filter(
            employee__employee_id=employee_id
        )

    if selected_month:
        try:
            year, month_number = selected_month.split('-')

            payrolls = payrolls.filter(
                month__year=int(year),
                month__month=int(month_number)
            )

        except (ValueError, TypeError):
            pass

    from employees.models import Employee

    employees = Employee.objects.all().order_by('employee_id')

    total_basic_salary = sum(
        payroll.basic_salary
        for payroll in payrolls
    )

    total_allowances = sum(
        payroll.allowances
        for payroll in payrolls
    )

    total_deductions = sum(
        payroll.deductions
        for payroll in payrolls
    )

    total_net_salary = sum(
        payroll.net_salary
        for payroll in payrolls
    )

    context = {
        'payrolls': payrolls,
        'employees': employees,
        'selected_employee': employee_id or '',
        'selected_month': selected_month or '',
        'total_basic_salary': total_basic_salary,
        'total_allowances': total_allowances,
        'total_deductions': total_deductions,
        'total_net_salary': total_net_salary,
    }

    return render(
        request,
        'payroll/payroll_report.html',
        context
    )