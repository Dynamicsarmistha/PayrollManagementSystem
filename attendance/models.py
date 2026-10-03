from django.db import models
from employees.models import Employee


class Attendance(models.Model):

    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Leave', 'Leave'),
    ]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )

    date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    remarks = models.CharField(
        max_length=255,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ('employee', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.employee.name} - {self.date} - {self.status}"


class Leave(models.Model):

    LEAVE_TYPE_CHOICES = [
        ('Casual Leave', 'Casual Leave'),
        ('Sick Leave', 'Sick Leave'),
        ('Earned Leave', 'Earned Leave'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='leave_records'
    )

    leave_type = models.CharField(
        max_length=30,
        choices=LEAVE_TYPE_CHOICES
    )

    from_date = models.DateField()

    to_date = models.DateField()

    reason = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.employee.name} - {self.leave_type}"