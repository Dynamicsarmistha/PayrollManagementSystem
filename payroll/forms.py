from django import forms
from .models import Payroll


class PayrollForm(forms.ModelForm):

    class Meta:
        model = Payroll
        fields = [
            'employee',
            'month',
            'basic_salary',
            'allowances',
            'deductions',
        ]

        widgets = {
            'employee': forms.Select(attrs={
                'class': 'form-select'
            }),

            'month': forms.DateInput(
            format='%Y-%m-%d',
            attrs={
            'type': 'date',
            'class': 'form-control'
    }
),

            'basic_salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter basic salary',
                'step': '0.01'
            }),

            'allowances': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter allowances',
                'step': '0.01'
            }),

            'deductions': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter deductions',
                'step': '0.01'
            }),
        }

    def save(self, commit=True):
        payroll = super().save(commit=False)

        payroll.net_salary = (
            payroll.basic_salary
            + payroll.allowances
            - payroll.deductions
        )

        if commit:
            payroll.save()

        return payroll