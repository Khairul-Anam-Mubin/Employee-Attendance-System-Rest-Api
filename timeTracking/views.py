from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
# Create your views here.

from timeTracking.services import CreateAttendanceService, MonthlyReportService 
from datetime import datetime
from calendar import monthrange
@csrf_exempt
def createAttendanceApi(request):
    if request.method == 'POST':
        req_data = JSONParser().parse(request)
        createAttendance = CreateAttendanceService(req_data)
        return JsonResponse(createAttendance.ServiceResponse(), safe=False)

@csrf_exempt
def monthlyReportApi(request):
    if request.method == 'POST':
        req_data = JSONParser().parse(request)
        monthlyReport = MonthlyReportService(req_data)
        return JsonResponse(monthlyReport.ServiceResponse(), safe= False)
    if request.method == 'GET':
        st_date = datetime.date(datetime.now())
        num_days = monthrange(st_date.year, st_date.month)[1]
        str_st_date = str(st_date.year)+"-"+str(st_date.month)+"-"+"01"
        str_end_date = str(st_date.year)+"-"+str(st_date.month) + "-"+ str(num_days)
        req_data = {
            'startDate' : str_st_date,
            'endDate' : str_end_date
        }
        monthlyReport = MonthlyReportService(req_data)
        return JsonResponse(monthlyReport.ServiceResponse(), safe= False)