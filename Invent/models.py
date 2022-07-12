from operator import length_hint
from tkinter import CASCADE, Widget
from django.db import models

# Create your models here.

EMP = (
    (1, 1),
    (2, 2),
    (3, 3)
)

CUST_NAME = (
    ("Cust1", "Cust1"),
    ("Cust2", "Cust2"),
    ("Cust3", "Cust3")
)
TASKS = [
    ("Turbine Maintanance","Turbine Maintanance"),
    ("Machine Review","Machine Review"),
    ("Budget Plan","Budget Plan"),
]

CATEGORY = (
    ("Addressable", "Addressable"),
    ("Unaddressable" , "Unaddressable"),
    ("Not-Applicable", "Not-Applicable")
)

CATEGORY1 = (
    ("Addressable", "Addressable"),
    ("Unaddressable" , "Unaddressable"),
    ("Not-Applicable", "Not-Applicable"),
    ("Don't Use This", "Don't Use This")
)

CATEGORY1_5 = (
    ("ISV-In UDI-Not in SFDC", "ISV-In UDI-Not in SFDC"),
    ("ISV-In SFDC-In UDI-Retain" , "ISV-In SFDC-In UDI-Retain"),
    ("GSV-Matching with SFDC", "GSV-Matching with SFDC"),
    ("GSV-Not in SFDCs", "GSV-Not in SFDCs"),
    ("GSV-Not in UDI", "GSV-Not in UDI")
)

CATEGORY2 = (
    ("Served", "Served"),
    ("Unserved", "Unserved")
)

CATEGORY3 = (
    ("ISV", "ISV"),
    ("GSV", "GSV")
)

CATEGORY4 = (
    ("OEM", "OEM"),
    ("oOEM", "oOEM")
)


SALES_TEAM = (
    ("West Sount", "West South"),
    ("East North", "East North")
)

class Task(models.Model):
    id = models.IntegerField(null=False)
    task_name = models.CharField(max_length=500, null=False, primary_key=True)
    target_definition = models.CharField(max_length=500, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    # duration = end_date-start_date
    # duration_days = duration.days
    

    def __str__(self) -> str:
        return self.task_name
    

class Employee(models.Model):
    #employee_ID - automatically comes in
    id = models.IntegerField(null=False, unique=True)
    employee_name = models.CharField(primary_key=True, max_length=200, null=False)

    def __str__(self) -> str:
        return self.employee_name
    

class Customer(models.Model):
    company_id = models.IntegerField(null=False, default=None)
    company = models.CharField(max_length=100, null=False, primary_key=True)
    parent = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.company

class CustomerInformation(models.Model):
    company = models.ForeignKey(Customer, on_delete=models.CASCADE, max_length=100, null=False)
    addressibility =  models.CharField(max_length=20, null=False, choices=CATEGORY)
    addressibility_calc =  models.CharField(max_length=20, null=False, choices=CATEGORY)
    served_unserved =  models.CharField(max_length=20, null=False, choices=CATEGORY2)
    BU = models.CharField(max_length=30, choices=CATEGORY3, null=False)
    unit = models.CharField(max_length=100, null=True)
    business_vertical = models.CharField(max_length=200, null=True)
    fleet_categorization = models.CharField(max_length=400, choices=CATEGORY1_5)
    ISV_fleet_BU_Input = models.IntegerField(null=True)

    def __str__(self) -> str:
        return str(self.company)

class AllotTask(models.Model):
    task_name = models.ForeignKey(Task, null=False, on_delete=models.CASCADE)
    employee_name = models.ForeignKey(Employee, null=False, on_delete=models.CASCADE)
    company = models.ForeignKey(Customer, null=False, default=None, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        lst = [self.task_name, self.employee_name, self.company] 
        return f"{lst[0]}:{lst[1]}:{lst[2]}"

class Team(models.Model):
    region = models.CharField(max_length=100, null=False)
    business_unit = models.CharField(max_length=200, null=False)
    sales_head_name = models.CharField(max_length=200)
    alloted_tasks = models.CharField(max_length=100, choices=TASKS)
    kpi = models.CharField(max_length=400, null=False)

    def __str__(self) -> str:
        return self.region

class BusinessPotential(models.Model):
    company = models.ForeignKey(Customer, on_delete=models.CASCADE)
    potential = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    addresable_market_INR = models.IntegerField(null=True)
    served_market_INR = models.IntegerField(null=True)
    OEM_oOEM = models.IntegerField(null=True, choices=CATEGORY4)

    def __str__(self) -> str:
        return self.company









    


    

