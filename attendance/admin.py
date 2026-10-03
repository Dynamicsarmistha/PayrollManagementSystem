from django.contrib import admin
from .models import Attendance, Leave


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):

    list_display = (
        'employee',
        'date',
        'status',
        'remarks',
    )

    list_filter = (
        'status',
        'date',
    )

    search_fields = (
        'employee__employee_id',
        'employee__name',
    )


@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):

    list_display = (
        'employee',
        'leave_type',
        'from_date',
        'to_date',
        'status',
    )

    list_filter = (
        'leave_type',
        'status',
    )

    search_fields = (
        'employee__employee_id',
        'employee__name',
    )