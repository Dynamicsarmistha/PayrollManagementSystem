from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AttendanceForm, LeaveForm
from .models import Attendance, Leave


@login_required
def attendance_list(request):

    records = Attendance.objects.select_related(
        'employee'
    ).all()

    return render(
        request,
        'attendance/attendance_list.html',
        {
            'records': records,
        }
    )


@login_required
def attendance_add(request):

    if request.method == 'POST':

        form = AttendanceForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Attendance added successfully.'
            )

            return redirect('attendance_list')

    else:
        form = AttendanceForm()

    return render(
        request,
        'attendance/attendance_form.html',
        {
            'form': form,
            'title': 'Mark Attendance',
        }
    )


@login_required
def attendance_edit(request, attendance_id):

    attendance = get_object_or_404(
        Attendance,
        id=attendance_id
    )

    if request.method == 'POST':

        form = AttendanceForm(
            request.POST,
            instance=attendance
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Attendance updated successfully.'
            )

            return redirect('attendance_list')

    else:
        form = AttendanceForm(
            instance=attendance
        )

    return render(
        request,
        'attendance/attendance_form.html',
        {
            'form': form,
            'title': 'Edit Attendance',
        }
    )


@login_required
def attendance_delete(request, attendance_id):

    attendance = get_object_or_404(
        Attendance,
        id=attendance_id
    )

    if request.method == 'POST':

        attendance.delete()

        messages.success(
            request,
            'Attendance deleted successfully.'
        )

        return redirect('attendance_list')

    return render(
        request,
        'attendance/attendance_confirm_delete.html',
        {
            'attendance': attendance,
        }
    )


@login_required
def leave_list(request):

    leaves = Leave.objects.select_related(
        'employee'
    ).all()

    return render(
        request,
        'attendance/leave_list.html',
        {
            'leaves': leaves,
        }
    )


@login_required
def leave_add(request):

    if request.method == 'POST':

        form = LeaveForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Leave request added successfully.'
            )

            return redirect('leave_list')

    else:
        form = LeaveForm()

    return render(
        request,
        'attendance/leave_form.html',
        {
            'form': form,
            'title': 'Add Leave Request',
        }
    )