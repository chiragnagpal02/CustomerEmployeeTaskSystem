from urllib.request import Request
from django.views.generic import CreateView
from django.shortcuts import render
from django.core import serializers
from .models import Customer, Employee, Task, AllotTask, CustomerInformation, BusinessPotential
from django.http import HttpResponse
from .forms import AllotTaskCreateForm, EmployeeCreateForm, CustomerCreateForm, CustomerInfoCreateForm, TaskCreateForm, TeamsCreateForm, PotentialCreateForm

# Create your views here.
# request -> response 

def index(request):
    return render(request, "dashboard/index.html")

def staff(request):
    return render(request, "dashboard/staff.html")

def order(request):
    return render(request, "dashboard/order.html")

def product(request):
    return render(request, "dashboard/product.html")

def customer_create_view(request):
    form = CustomerCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CustomerCreateForm()

    context = {
        'form': form
    }
    return render(request, "dashboard/forms/customer.html", context)

def customer_info_create_view(request):
    form = CustomerInfoCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CustomerInfoCreateForm()

    context = {
        'form': form
    }
    return render(request, "dashboard/forms/CustomerInfo.html", context)

def potential_create_view(request):
    form = PotentialCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PotentialCreateForm()

    context = {
        'form': form
    }
    return render(request, "dashboard/forms/potential.html", context)

def team_create_view(request):
    form = TeamsCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TeamsCreateForm()


    context = {
        'form': form
    }
    return render(request, "dashboard/forms/team.html", context)

def task_create_view(request):
    form = TaskCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TaskCreateForm()
    
    context = {
        'form': form
    }
    return render(request, "dashboard/forms/task.html", context)

def allot_task_create_view(request):
    form = AllotTaskCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AllotTaskCreateForm()
    
    context = {
        'form': form
    }
    return render(request, "dashboard/forms/allot_task.html", context)

def employee_create_view(request):
    form = EmployeeCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = EmployeeCreateForm()

    context = {
        'form': form
    }
    return render(request, "dashboard/forms/employee.html", context)


def task_detail_view(request):
    data = serializers.serialize("python", Task.objects.all())
    context = {
        'data': data
    }
    print(data)

    return render(request, "dashboard/display/dtask.html", context)

def allot_task_detail_view(request):
    data = serializers.serialize("python", AllotTask.objects.all())
    context = {
        'data': data
    }
    print(data)

    return render(request, "dashboard/display/dallot_task.html", context)

def employee_detail_view(request):
    data = serializers.serialize("python", Employee.objects.all())
    context = {
        'data': data
    }

    return render(request, "dashboard/display/demployee.html", context)

def customer_detail_view(request):
    data = serializers.serialize("python", Customer.objects.all())
    context = {
        'data': data
    }

    return render(request, "dashboard/display/dcustomer.html", context)

def potential_detail_view(request):
    data = serializers.serialize("python", BusinessPotential.objects.all())
    context = {
        'data': data
    }

    return render(request, "dashboard/display/dpotential.html", context)

def customer_info_detail_view(request):
    data = serializers.serialize("python", CustomerInformation.objects.all())
    context = {
        'data': data
    }

    return render(request, "dashboard/display/dcustomerinfo.html", context)

def customer_details(request):
    return render(request, "dashboard/display/giveCust.html")

def find_customer_details(request):
    context_dict = {}
    if request.method == 'POST':
        search_id = request.POST.get('cust_id', None)
        user = Customer.objects.get(id=search_id)
        if search_id:
            context_dict['result'] = user
        else:
            context_dict['no_result'] = search_id

    return render(request, "dashboard/display/giveCust.html", context_dict)


