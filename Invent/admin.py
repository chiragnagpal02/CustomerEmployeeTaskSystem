from django.contrib import admin
from .models import Customer, CustomerInformation, Task, Employee, Team, BusinessPotential, AllotTask
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class CustomerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class CustomerInformationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class PotentialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class TaskAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class AllotTaskAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class EmployeeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class TeamAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(CustomerInformation, CustomerInformationAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(AllotTask, AllotTaskAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(BusinessPotential, PotentialAdmin)


#@admin.register(Desktop, Mobile, Laptop)

