from django.forms import ModelForm, TextInput, Select
from .models import Tools, Rental, Employee
from django import forms


class ToolForm(ModelForm):
    class Meta:
        model = Tools
        fields = ['name', 'active']


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'active']


class RentalForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RentalForm, self).__init__(*args, **kwargs)
        self.fields['tools'] = forms.ModelChoiceField(queryset=Tools.objects.filter(active=True))
        self.fields['employee'] = forms.ModelChoiceField(queryset=Employee.objects.filter(active=True))

    class Meta:
        model = Rental
        fields = ['tools', 'employee', 'description', 'date_of_rent', 'date_of_return']

