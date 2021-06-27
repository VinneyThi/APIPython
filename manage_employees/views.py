from .models import Employee
from .serializer import EmployeeSerializer
from django.http import HttpResponse
import json, re
from rest_framework.parsers import JSONParser


# Create your views here.




def employee(request,emailKey=''):
   
    

    if request.method == 'GET' and emailKey=='':
        employees =   Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return HttpResponse(json.dumps(serializer.data))

    elif request.method =='POST':
        
            employeeAux = json.loads(request.body)
            try:
                if employeeAux['name'] =='' or  re.search (r'.*@.*\..*',employeeAux['email']) == None  or employeeAux['department'] == '':
                    return HttpResponse("fields invalid")
                findEmployee = Employee.objects.get(email=employeeAux['email'])
                
                return HttpResponse("Email existed in database")
            except (IndexError,KeyError) as erro:
                return HttpResponse('fields invalid') 
            except Employee.DoesNotExist :
                newEmployee = Employee(name= employeeAux['name'],email= employeeAux['email'], department= employeeAux['department'])
                newEmployee.save()
                return HttpResponse("success") 
    elif request.method =='DELETE':
           
            try:
                if emailKey =='' or  re.search (r'.*@.*\..*',emailKey) == None:
                    return HttpResponse("Email invalid")

                findEmployee = Employee.objects.get(email=emailKey)
                findEmployee.delete()
                return HttpResponse("sucesso")
            except (IndexError,KeyError) as erro:
                return HttpResponse('input invalid')
            except Employee.DoesNotExist as erro:
                return HttpResponse('email does not exist')
            
    
    return HttpResponse('router invalid') 

                
       
   

    