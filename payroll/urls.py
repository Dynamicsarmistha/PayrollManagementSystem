from django.urls import path
from . import views


urlpatterns = [
    path('', views.payroll_list, name='payroll_list'),

    path('add/', views.payroll_add, name='payroll_add'),

    path('edit/<int:payroll_id>/', views.payroll_edit, name='payroll_edit'),

    path('delete/<int:payroll_id>/', views.payroll_delete, name='payroll_delete'),

    path(
    'salary-slip/<int:payroll_id>/',
    views.salary_slip,
    name='salary_slip'
),

path(
    'attendance-salary/<int:payroll_id>/',
    views.attendance_salary,
    name='attendance_salary'
),


path('reports/', views.payroll_report, name='payroll_report'),

]