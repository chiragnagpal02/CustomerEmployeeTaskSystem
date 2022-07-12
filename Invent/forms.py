from django import forms


from .models import Employee, Customer, Task, Team, BusinessPotential, AllotTask, CustomerInformation


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'id',
            'employee_name'
        ]

class PotentialCreateForm(forms.ModelForm):
    class Meta:
        model = BusinessPotential
        skip_unchanged = True
        report_skipped = True
        fields = [
            'company',
            'potential',
            'addresable_market_INR',
            'served_market_INR',
            'year',
            'OEM_oOEM',
        ]


class CustomerInfoCreateForm(forms.ModelForm):
    class Meta:
        model = CustomerInformation
        
        fields = [
            'company',
            'served_unserved',
            'addressibility',
            'addressibility_calc',
            'BU',
            'unit',
            'business_vertical',
            'fleet_categorization',
            'ISV_fleet_BU_Input'
        ]

class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        
        fields = [
            'company_id',
            'company',
            'parent',
        ]


class AllotTaskCreateForm(forms.ModelForm):
    class Meta:
        model = AllotTask
        fields = [
            'task_name',
            'company',
            'employee_name',
        ]     

class TeamsCreateForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            'region',
            'business_unit',
            'sales_head_name',
            'alloted_tasks',
            'kpi'
        ]  

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'id',
            'task_name',
            'start_date',
            'end_date',
            'target_definition'
        ]       
     
       
        
        
        
        
    
