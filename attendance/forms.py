from django import forms
from .models import Attendance, Leave


class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance

        fields = [
            'employee',
            'date',
            'status',
            'remarks',
        ]

        widgets = {
            'employee': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            'status': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'remarks': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter remarks (optional)'
                }
            ),
        }


class LeaveForm(forms.ModelForm):

    class Meta:
        model = Leave

        fields = [
            'employee',
            'leave_type',
            'from_date',
            'to_date',
            'reason',
            'status',
        ]

        widgets = {
            'employee': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'leave_type': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'from_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            'to_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            'reason': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Enter reason for leave'
                }
            ),

            'status': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
        }