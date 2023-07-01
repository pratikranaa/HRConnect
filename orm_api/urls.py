from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from drf_yasg import openapi
from .views import *

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Employee ORM API",
        default_version='v1',
        description="API documentation of ORM app",
        ),
    public=True,
    # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('employees/', get_employees, name='api_employees'),
    path('employee/<int:employee_id>/', get_employee, name='api_get_employee'),
    path('employee/create/', create_employee, name='api_create_employee'),
    path('employee/<int:employee_id>/update/', update_employee, name='api_update_employee'),
    path('employee/<int:employee_id>/delete/', delete_employee, name='api_delete_employee'),
    path('employees/designation/<str:designation>/', get_employees_by_designation, name='api_get_employees_by_designation'),
    path('employees/salary/higher/<int:min_salary>/', get_employees_with_high_salary, name='api_get_employees_with_high_salary'),
    path('employees/name/<str:name>/', get_employees_by_name, name='api_get_employees_by_name'),
    path('employees/salary/range/<int:min_salary>/<int:max_salary>/', get_employees_by_salary_range, name='api_get_employees_by_salary_range'),
    path('employees/ids/<str:employee_ids>/', get_employees_by_ids, name='api_get_employees_by_ids'),
    path('employees/designation/<str:designation>/salary/higher/<int:min_salary>/', get_employees_by_designation_and_salary, name='api_get_employees_by_designation_and_salary'),
    path('employees/exclude/designation/<str:designation>/', exclude_employees_by_designation, name='api_exclude_employees_by_designation'),
    path('employees/order/salary/', order_employees_by_salary, name='api_order_employees_by_salary'),
    path('employees/count/', get_employee_count, name='api_get_employee_count'),
    path('employee/exists/<int:employee_id>/', check_employee_exists, name='api_check_employee_exists'),
    path('employees/fields/', get_employees_fields, name='api_get_employees_fields'),
    path('employees/avg-salary/', annotate_avg_salary, name='api_annotate_avg_salary'),
    path('employees/bulk-update/', bulk_update_employees, name='api_bulk_update_employees'),
    path('employees/bulk-create/', bulk_create_employees, name='api_bulk_create_employees'),
    path('employees/total-salary/', get_total_salary, name='api_get_total_salary'),


    #path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Add other URLs if needed
]

