import re
from account.models import Employees
from account.serializers import EmployeeSerializer

class CreateAccountService:
    def __init__(self,  reqData):
        self.accountData = reqData
    def IsReqDataValid(self):
        key_list = ["EmployeeId",
        "EmployeeFirstName", 
        "EmployeeLastName",
        "EmployeeDesignation",
        "EmployeeAddress",
        "EmployeePhoneNumber",
        "EmployeeEmail",
        "EmployeePin"]
        if len(key_list) != len(self.accountData):
            return False
        for key in key_list:
            if key not in self.accountData:
                return False
        return True
    def IsUniqueId(self): #Two Employee id can't be same.
        countData = Employees.objects.filter(EmployeeId = self.accountData['EmployeeId']).count()
        if countData != 0:
            return False
        return True
    def IsUniqueEmail(self): #Two employee email can't be same.
        countData = Employees.objects.filter(EmployeeEmail = self.accountData['EmployeeEmail']).count()
        if countData != 0:
            return False
        return True
    def IsUniquePhoneNumber(self): #Two employee Phone Numbmer can't be same.
        countData = Employees.objects.filter(EmployeePhoneNumber = self.accountData['EmployeePhoneNumber']).count()
        if countData != 0:
            return False
        return True
    def SelectAccountType(self): 
        if Employees.objects.all().count() != 0:
            self.accountData['EmployeeRole'] = "member"
        else:
            self.accountData['EmployeeRole'] = "admin"
    def IsPossibleToInsertDB(self):
        employee_serializer = EmployeeSerializer(data = self.accountData)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return True
        return False
    def ServiceResponse(self):
        if self.IsReqDataValid() and self.IsUniqueId() and self.IsUniqueEmail() and self.IsUniquePhoneNumber():
            self.SelectAccountType()
            if self.IsPossibleToInsertDB():
                return self.accountData
        return None

class ShowEmployeeService:
    def __init__(self, employeeId):
        self.employeeId = employeeId
        pass
    def ServiceResponse(self):
        if self.employeeId == None:
            employees = Employees.objects.all()
            employees_serializer = EmployeeSerializer(employees, many = True)
            return employees_serializer.data
        else:
            try:
                employee = Employees.objects.get(EmployeeId = self.employeeId) #check needed
            except Employees.DoesNotExist:
                return None
            employee_serializer = EmployeeSerializer(employee)
            return employee_serializer.data