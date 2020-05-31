from django.forms import ModelForm, TextInput, Select
from .models import Tools, Rental, Employee


class ToolForm(ModelForm):
    class Meta:
        model = Tools
        fields = ['name', 'active']


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'active']


class RentalForm(ModelForm):
    class Meta:
        model = Rental
        fields = ['tools', 'employee', 'description', 'date_of_rent', 'date_of_return']

