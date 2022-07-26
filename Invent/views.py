
from multiprocessing import context, managers
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import requests
from django.core import serializers
from .models import Customer, Employee, Task, AllotTask, CustomerInformation, BusinessPotential
from django.http import HttpResponse
from .forms import AllotTaskCreateForm, EmployeeCreateForm, CustomerCreateForm, CustomerInfoCreateForm, TaskCreateForm, TeamsCreateForm, PotentialCreateForm, CreateUserForm



API_KEY = "1ec33832bb424bee9d5f39dd9aba6204"
# Create your views here.
# request -> response 

def registerPage(request):
    form = CreateUserForm() 

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {
        "form" : form
        }
    return render(request, "dashboard/forms/register.html", context)

def loginPage(request):

    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        user = authenticate(request, username = username, password = password)


        if user is not None:
            login(request, user)
            return redirect('index')
        else :
             messages.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, "dashboard/forms/login.html", context) 

def logoutUser(request):
    return redirect('login')

def give_news(request):

    url = f'https://newsapi.org/v2/top-headlines?category=science&country=in&from=2022-07-13&sortBy=popularity&apiKey={API_KEY}'

    response = requests.get(url)
    data = response.json()

    articles = data['articles']

    context = {
        'articles' : articles,
        'data' : data
    }

    return render(request, "dashboard/display/news.html", context)


def index(request):
    emp_count = Employee.objects.count()
    cust_count = Customer.objects.count()
    task_count = Task.objects.count()

    context = {
        'empcount' : emp_count,
        'custcount' : cust_count,
        'taskcount' : task_count
    }

    return render(request, "dashboard/index.html", context)

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

def dashboard(request):
    return render(request, "dashboard/forms/dashboard.html")

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
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            name = f"{request.user.first_name.title()} {request.user.last_name.title()}" 
            print(name)
            post.manager_name = name
            post.save()
            form = EmployeeCreateForm()
    # form = EmployeeCreateForm(request.POST or None)
    # if form.is_valid():
    #     # obj = form.save(commit=False) # Return an object without saving to the DB
    #     name = request.user.first_name.title
    #     print(name)
    #     print(form['manager_name'].value())
    #     form.data['manager_name'] = name # Add an author field which will contain current user's id
    #     form.save() # Save the final "real form" to the DB
    #     form = EmployeeCreateForm()

    context = {
        'form' : form
    }

    # if request.method == "POST":
    #     if request.user.is_authenticated:

    #         form = EmployeeCreateForm(request.POST)

    #         if form.is_valid():
    #             obj = form.save(commit=False) # Return an object without saving to the DB
    #             obj.manager_name = User.objects.get(pk=request.user.id) # Add an author field which will contain current user's id
    #             obj.save() # Save the final "real form" to the DB
    #             form = EmployeeCreateForm()
    #             # context = {'form':form}
    #         else:
    #             print("ERROR : Form is invalid")
    #             print(form.errors)

    
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


def customer_specific_by_parent(request):
    if request.method == "POST":
        parent_new = request.POST.get('new_parent')
        print(parent_new)
        data = Customer.objects.filter(parent__icontains = parent_new)
        print(data)
        ids = []

        # for query in data:
        #     if len(data) > 1:
        #         id = Customer.objects.get()

        context = {
            'data' : data,
        }

        return render(request, "dashboard/display/finale.html", context)

def customer_specific_by_company(request):
    if request.method == "POST":
        company_new = request.POST.get('new_company')
        dta = Customer.objects.filter(company__icontains = company_new)
        ids = []

        # for query in data:
        #     if len(data) > 1:
        #         id = Customer.objects.get()
        
        print(dta)

        context = {
            'data' : dta,
            'company' : company_new
        }

        return render(request, "dashboard/display/finale_c.html", context)

def employee_specific_by_manager(request):
    if request.method == "POST":
        manager_new = request.POST.get('new_manager')
        data = Employee.objects.filter(manager_name__icontains = manager_new)

        # for query in data:
        #     if len(data) > 1:
        #         id = Customer.objects.get()
        
        print(data)

        context = {
            'data' : data,
            
        }

        return render(request, "dashboard/display/finale_m.html", context)

    
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

def dashboard_statistics(request):
    emp_count = Employee.objects.count()
    cust_count = Customer.objects.count()
    task_count = Task.objects.count()

    context = {
        'empcount' : emp_count,
        'custcount' : cust_count,
        'taskcount' : task_count
    }

    return render(request, "dashboard/forms/dashboard.html", context)