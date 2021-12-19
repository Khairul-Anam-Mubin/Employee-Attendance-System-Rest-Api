from timeTracking.models import Attendances
from timeTracking.serializers import AttendanceSerializer
from account.models import Employees


class CreateAttendanceService:
    def __init__(self, reqData):
        self.attendance = reqData
    def IsReqDataValid(self):
        key_list = [
            "EmployeeId",
            "EmployeePin",
            "SuiteNumber",
            "Status"
        ]
        if len(key_list) != len(self.attendance):
            return False
        for key in key_list:
            if key not in self.attendance:
                return False
        if self.attendance['Status'] == "exit" or self.attendance['Status'] == "entry":
            print("Valid req")
            return True
        print("InValid req")
        print(self.attendance)
        return False
    def IsEmployeeIdAndPinValid(self):
        try :
            employee_data = Employees.objects.get(EmployeeId = self.attendance['EmployeeId'], EmployeePin = self.attendance['EmployeePin'])
        except Employees.DoesNotExist:
            return False
        self.attendance.pop('EmployeePin', None)
        print("pin valid")
        return True
    def IsPossibleToInsertDB(self):
        if Attendances.objects.filter(EmployeeId = self.attendance['EmployeeId']).count() == 0:
            attendance_serializer = AttendanceSerializer(data = self.attendance)
            if attendance_serializer.is_valid():
                attendance_serializer.save()
                return True
            return False 
        #print("here")
        last_attendance_data = AttendanceSerializer(Attendances.objects.filter(EmployeeId = self.attendance['EmployeeId']).last()).data
        #print(self.attendance)
        #print(last_attendance_data)
        if last_attendance_data['Status'] != self.attendance['Status']:
            attendance_serializer = AttendanceSerializer(data = self.attendance)
            if attendance_serializer.is_valid():
                attendance_serializer.save()
                #print("inserted")
                return True
            return False
        #print("not inserted")
        return False
    def ServiceResponse(self):
        if self.IsReqDataValid():
            #print("Valid")
            if self.IsEmployeeIdAndPinValid() and self.IsPossibleToInsertDB():
                #print("ok")
                return self.attendance
        return None

class MonthlyReportService:
    def __init__(self, reqData):
        self.reqData = reqData
        self.all_employees = Employees.objects.all()
    def IsValidData(self):
        key_list = [
            'startDate',
            'endDate'
        ]
        if len(self.reqData) != len(key_list):
            return False
        for key in key_list:
            if key not in self.reqData:
                return False
        #print("ok")
        return True
    def MonthlyReportById(self, employeeId):
        found_employee = False
        employee_firstName = ""
        employee_lastName = ""
        for employee in self.all_employees:
            if employee.EmployeeId == employeeId:
                employee_firstName = employee.EmployeeFirstName
                employee_lastName = employee.EmployeeLastName
                found_employee = True
                break
        if found_employee == False:
            return None
        all_data_by_date = Attendances.objects.filter(AccessDate__range = [str(self.reqData['startDate']), str(self.reqData['endDate'])])
        data_list_id = []
        for data in all_data_by_date:
            if data.EmployeeId == employeeId:
                data_list_id.append(data)
        if len(data_list_id) <= 1:
            return None
        total_sec = 0
        for i in range(0 , len(data_list_id) - 1, 2):
            time1 = str(data_list_id[i].AccessTime).split('.')[0]
            sec1 = sum(x * int(t) for x, t in zip([3600, 60, 1], time1.split(":"))) 
            time2 = str(data_list_id[i + 1].AccessTime).split('.')[0]
            sec2 = sum(x * int(t) for x, t in zip([3600, 60, 1], time2.split(":")))
            dif_sec = sec2 - sec1
            total_sec += dif_sec
        h = total_sec // 3600
        total_sec %= 3600
        m = total_sec // 60
        total_sec %= 60
        s = total_sec
        total_stay_time = str(h) + ":" + str(m) + ":" + str(s)
        entryTime = str(data_list_id[0].AccessDate) +"T" + str(data_list_id[0].AccessTime)
        exitTime =  str(data_list_id[-1].AccessDate) + "T" + str(data_list_id[-1].AccessTime)
        postData = {
            'EmployeeId' : employeeId,
            'EmployeeFirstName' : employee_firstName,
            'EmployeeLastName' : employee_lastName,
            'EntryTime': entryTime,
            'ExitTime': exitTime,
            'TotalStayTime' : total_stay_time
        }
        return postData
    def MonthlyReport(self):
        all_data_group = {}
        all_data = Attendances.objects.filter(AccessDate__range = [str(self.reqData['startDate']), str(self.reqData['endDate'])])
        item = 1
        for data in self.all_employees:
            postData = self.MonthlyReportById(data.EmployeeId)
            if postData != None:
                all_data_group[item] = postData
                item += 1
        #print(all_data_group)
        return all_data_group
    def ServiceResponse(self):
        if self.IsValidData():
            return self.MonthlyReport()
        return None    