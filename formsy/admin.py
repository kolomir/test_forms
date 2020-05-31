from django.contrib import admin
from .models import Tools, Employee, Rental

# Register your models here.
@admin.register(Tools)
class ToolsAdmin(admin.ModelAdmin):
    list_display = ('name', 'active') # lista dodanych pozycji - wymienione kolumny
    list_filter = ('name', 'active') #dostępne filtrowania
    search_fields = ('name', 'active') #możliwość wyszukiwania


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'active') # lista dodanych pozycji - wymienione kolumny
    list_filter = ('name', 'active') #dostępne filtrowania
    search_fields = ('name', 'active') #możliwość wyszukiwania


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('tools', 'employee', 'description', 'date_of_rent', 'date_of_return') # lista dodanych pozycji - wymienione kolumny
    list_filter = ('tools', 'employee', 'description', 'date_of_rent', 'date_of_return') #dostępne filtrowania
    search_fields = ('tools', 'employee', 'description', 'date_of_rent', 'date_of_return') #możliwość wyszukiwania