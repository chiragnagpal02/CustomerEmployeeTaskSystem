from typing import Type
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import Employee, Customer, Task, Team, BusinessPotential, AllotTask, CustomerInformation


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'id',
            'employee_name',
            # 'manager_name',
        ]

class PotentialCreateForm(forms.ModelForm):
    class Meta:
        model = BusinessPotential
        # skip_unchanged = True
        # report_skipped = True
        fields = [
            'company',
            'potential',
            'addresable_market_INR',
            'served_market_INR',
            'total_market_INR',
            'year',
            'OEM_oOEM',
        ]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'username', 
            'email', 
            'password1', 
            'password2',
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
            'cr_status'
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
        # field_classes = {
        #     'region': "form-control",
        # }
    
        # widgets = {
        #     # 'region' : (attrs={'class':'form-control'}),
        #     # 'business_unit' : type(attrs={'class':'form-control'}),
        #     # 'sales_head_name' : type(attrs={'class':'form-control'}),
        #     # 'alloted_tasks' : type(attrs={'class':'form-control'}),
                     
        # } 


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
        widgets = {
            'start_date' : forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'end_date' : forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        } 
     
       
        
        
        
        
    
