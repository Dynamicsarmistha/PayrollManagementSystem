from django.contrib import admin
from .models import Department, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
    )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = (
        'employee_id',
        'name',
        'email',
        'phone',
        'department',
        'designation',
        'basic_salary',
    )

    search_fields = (
        'employee_id',
        'name',
        'email',
    )
