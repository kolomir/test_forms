from django.urls import path
from .views import new_tool, new_employee, new_rental, tools_list, employee_list, rental_list


urlpatterns = [
    path('tools/', tools_list, name='tools'),
    path('tools_form/', new_tool, name='new_tool'),
    path('employee/', employee_list, name='employee'),
    path('employee_form/', new_employee, name='new_employee'),
    path('rental/', rental_list, name='rental'),
    path('rental_form/', new_rental, name='new_rental'),
]