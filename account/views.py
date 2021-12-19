from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
# Create your views here.

from account.services import CreateAccountService, ShowEmployeeService

@csrf_exempt
def createAccountApi(request):
    if request.method == 'POST':
        employee_data = JSONParser().parse(request) 
        createAccount = CreateAccountService(employee_data)
        return JsonResponse(createAccount.ServiceResponse(), safe = False)

@csrf_exempt
def showEmployeeApi(request, pk = None):
    if request.method == 'GET':
        showEmployee = ShowEmployeeService(pk)
        return JsonResponse(showEmployee.ServiceResponse(), safe = False)
