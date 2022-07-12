from django.urls import path 
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('staff/', views.staff, name='staff'), 
    path('order/', views.order, name='order'),
    path('product/', views.product, name='product'),
    path('customer/', views.customer_create_view, name='customer'),
    path('customerInfo/', views.customer_info_create_view, name='customerinfo'),
    path('employee/', views.employee_create_view, name='employee'),
    path('task/', views.task_create_view, name='task'),
    path('allottask/', views.allot_task_create_view, name='allot_task'),
    path('team/', views.team_create_view, name='team'),
    path('dtask/', views.task_detail_view, name='dtask'),
    path('dallot_task/', views.allot_task_detail_view, name='dallot_task'),
    path('demployee/', views.employee_detail_view, name='demployee'),
    path('dcustomer/', views.customer_detail_view, name='dcustomer'),
    path('dcustomerinfo/', views.customer_info_detail_view, name='dcustomerinfo'),
    path('givec/', views.customer_details, name='details'),
    path('givec/post/', views.find_customer_details, name='details'),
    path('potential/', views.potential_create_view, name='potentials'),
    path('dpotential/', views.potential_detail_view, name='dpotential'),
]