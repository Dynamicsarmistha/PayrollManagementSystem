from django.urls import path

from . import views


urlpatterns = [
    path(
        '',
        views.attendance_list,
        name='attendance_list'
    ),

    path(
        'add/',
        views.attendance_add,
        name='attendance_add'
    ),

    path(
        'edit/<int:attendance_id>/',
        views.attendance_edit,
        name='attendance_edit'
    ),

    path(
        'delete/<int:attendance_id>/',
        views.attendance_delete,
        name='attendance_delete'
    ),

    # Leave Management
    path(
        'leaves/',
        views.leave_list,
        name='leave_list'
    ),

    path(
        'leaves/add/',
        views.leave_add,
        name='leave_add'
    ),
]