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
    def IsUniqueId(self):
        try:
            getdata = Employees.objects.get(EmployeeId = self.accountData['EmployeeId'])
        except Employees.DoesNotExist:
            return True
        return False
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
        if self.IsReqDataValid() and self.IsUniqueId():
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