from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .employee_serializer import *

# Create your views here.

@api_view(['GET'])
def get_employees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Employee created', 'data': serializer.data}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_employee(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    except Employee.DoesNotExist:
        return Response({'message': 'Employee not found'}, status=404)

@api_view(['PUT'])
def update_employee(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except Employee.DoesNotExist:
        return Response({'message': 'Employee not found'}, status=404)

@api_view(['DELETE'])
def delete_employee(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
        employee.delete()
        return Response({'message': 'Employee deleted'})
    except Employee.DoesNotExist:
        return Response({'message': 'Employee not found'}, status=404)

@api_view(['GET'])
def get_employees_by_designation(request, designation):
    employees = Employee.objects.filter(designation=designation)
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_employees_with_high_salary(request, min_salary):
    employees = Employee.objects.filter(salary__gt=min_salary)
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_employees_by_name(request, name):
    employees = Employee.objects.filter(name__iexact=name)
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_employees_by_salary_range(request, min_salary, max_salary):
    employees = Employee.objects.filter(salary__range=(min_salary, max_salary))
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_employees_by_ids(request, employee_ids):
    ids_list = employee_ids.split(',')
    employees = Employee.objects.filter(id__in=ids_list)
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_employees_by_designation_and_salary(request, designation, min_salary):
    employees = Employee.objects.filter(designation=designation, salary__gt=min_salary)
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def exclude_employees_by_designation(request, designation):
    employees = Employee.objects.exclude(designation=designation)
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def order_employees_by_salary(request):
    employees = Employee.objects.order_by('-salary')
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_employee_count(request):
    count = Employee.objects.count()
    return Response({'count': count})

@api_view(['GET'])
def check_employee_exists(request, employee_id):
    exists = Employee.objects.filter(id=employee_id).exists()
    return Response({'exists': exists})

@api_view(['GET'])
def get_employees_fields(request):
    employees = Employee.objects.values('name', 'designation')
    return Response(employees)



from django.db.models import Avg

@api_view(['GET'])
def annotate_avg_salary(request):
    data = Employee.objects.values('designation').annotate(avg_salary=Avg('salary'))
    return Response(data)
    
@api_view(['PUT'])
def bulk_update_employees(request):
    employee_data = request.data.get('employees', [])
    employee_ids = [data['id'] for data in employee_data]
    employees = Employee.objects.filter(id__in=employee_ids)

    for employee, data in zip(employees, employee_data):
        serializer = EmployeeSerializer(employee, data=data)
        if serializer.is_valid():
            serializer.save()

    return Response({'message': 'Employees updated'})

@api_view(['POST'])
def bulk_create_employees(request):
    employee_data = request.data.get('employees', [])
    employees = [Employee(**data) for data in employee_data]
    Employee.objects.bulk_create(employees)
    return Response({'message': 'Employees created'}, status=201)

from django.db.models import Sum

@api_view(['GET'])
def get_total_salary(request):
    total_salary = Employee.objects.aggregate(total_salary=Sum('salary'))
    return Response(total_salary)









# @api_view(['GET'])
# def get_employee(request, employee_id):
#     try:
#         employee = Employee.objects.get(id=employee_id)
#         data = {
#             'employee id': employee.id,
#             'name': employee.name,
#             'phone': employee.phone,
#             'email': employee.email,
#             'designation': employee.designation,
#             'salary': str(employee.salary),
#             'address': employee.address
#         }
#         return Response(data)
#     except Employee.DoesNotExist:
        # return Response(status=404)

# @api_view(['POST'])
# def create_employee(request):
#     name = request.data.get('name')
#     phone = request.data.get('phone')
#     email = request.data.get('email')
#     designation = request.data.get('designation')
#     salary = request.data.get('salary')
#     address = request.data.get('address')

#     employee = Employee.objects.create(name=name, phone=phone, email=email, designation=designation, salary=salary, address=address)
#     data = {
#         'employee id': employee.id,
#         'name': employee.name,@api_view(['POST'])
# def create_employee(request):
#     name = request.data.get('name')
#     phone = request.data.get('phone')
#     email = request.data.get('email')
#     designation = request.data.get('designation')
#     salary = request.data.get('salary')
#     address = request.data.get('address')

#     employee = Employee.objects.create(name=name, phone=phone, email=email, designation=designation, salary=salary, address=address)
#     data = {
#         'employee id': employee.id,
#         'name': employee.name,
#         'phone': employee.phone,
#         'email': employee.email,
#         'designation': employee.designation,
#         'salary': str(employee.salary),
#         'address': employee.address
#     }
#     return Response(data, status=201)
#         'phone': employee.phone,
#         'email': employee.email,
#         'designation': employee.designation,
#         'salary': str(employee.salary),
#         'address': employee.address
#     }
#     return Response(data, status=201)





# def get_employees(request):
#     employees = Employee.objects.all()
#     data = {
#         'employee': [
#             {
                
#                 'employee id': e.id,
#                 'name': e.name, 
#                 'phone': e.phone, 
#                 'email':e.email, 
#                 'designation': e.designation, 
#                 'salary': str(e.salary),
#                 'address': e.address 
#                 } for e in employees
#             ]
#     }
#     return JsonResponse(data)