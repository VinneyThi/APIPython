from .models import Employee
from .serializer import EmployeeSerializer
from django.http import HttpResponse
import json, re
from rest_framework.parsers import JSONParser


# Create your views here.




def employee(request):
    employees =   Employee.objects.all()
    serializer = EmployeeSerializer(employees,many=True)
    

    if request.method == 'GET':
        return HttpResponse(json.dumps(serializer.data))

    elif request.method =='POST':
        
            employeeAux = json.loads(request.body)
            try:
                if employeeAux['name'] =='' or  re.search (r'.*@.*\..*',employeeAux['email']) == None  or employeeAux['department'] == '':
                    return HttpResponse("fields invalid")

                newEmployee = Employee(name= employeeAux['name'],email= employeeAux['email'], department= employeeAux['department'])
                newEmployee.save()
                return HttpResponse("sucesso")
            except (IndexError,KeyError) as erro:
                return HttpResponse(erro) 
    elif request.method =='DELETE':
            print(request.body)
            # employeeAux = json.loads(request.body)
            # try:
            #     if employeeAux['name'] =='' or  re.search (r'.*@.*\..*',employeeAux['email']) == None  or employeeAux['department'] == '':
            #         return HttpResponse("fields invalid")

            #     newEmployee = Employee(name= employeeAux['name'],email= employeeAux['email'], department= employeeAux['department'])
            #     newEmployee.save()
            #     return HttpResponse("sucesso")
            # except (IndexError,KeyError) as erro:
            #     return HttpResponse(erro) 

                
       
   
