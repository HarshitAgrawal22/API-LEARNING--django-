from django.contrib import admin
from .models import company,employee

class CompanyAdmin(admin.ModelAdmin):
    list_display=("name","location","type") # these are the things which will be displayed
    search_fields=("name","id")# these are the things with chich help we can search a company

class EmployeeAdmin(admin.ModelAdmin):
    list_display=("name","email","company")# things to display
    list_filter=("company",)#filter option to filter the employee on the basis of company

admin.site.register(company,CompanyAdmin)
admin.site.register(employee,EmployeeAdmin)

