from django import forms
from Employee.models import empTable


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = empTable
        fields = "__all__"
