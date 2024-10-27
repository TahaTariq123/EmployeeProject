"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from app.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'start_salary', 'current_salary', 'years_of_experience', 'date_of_joining']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'start_salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'current_salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'years_of_experience': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_of_joining': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }