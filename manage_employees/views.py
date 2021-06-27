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

    elif request.method =='POST' and emailKey =='':
        
            employeeAux = json.loads(request.body)
            try:
                if employeeAux['name'] =='' or  re.search (r'.*@.*\..*',employeeAux['email']) == None  or employeeAux['department'] == '':
                    return HttpResponse("{text:fields invalid, Httpcode:400}")
                findEmployee = Employee.objects.get(email=employeeAux['email'])
                
                return HttpResponse("{text:Email existed in database, Httpcode:202}")
            except (IndexError,KeyError) as erro:
                return HttpResponse("{text:fields invalid, Httpcode:400}") 
            except Employee.DoesNotExist :
                newEmployee = Employee(name= employeeAux['name'],email= employeeAux['email'], department= employeeAux['department'])
                newEmployee.save()
                return HttpResponse('{text:created, Httpcode:201}') 
    elif request.method =='DELETE':
           
            try:
                if emailKey =='' or  re.search (r'.*@.*\..*',emailKey) == None:
                    return HttpResponse('{text:Email invalid, Httpcode:400}')

                findEmployee = Employee.objects.get(email=emailKey)
                findEmployee.delete()
                return HttpResponse('{text:ok, Httpcode:200}')
            except (IndexError,KeyError) as erro:
                return HttpResponse('{text:input invalid, Httpcode:400}')
            except Employee.DoesNotExist as erro:
                return HttpResponse("{'text':'email does not exist', 'Httpcode':'400'}")
            
    
    return HttpResponse("{'text':'NOT Found', 'Httpcode':'404'}") 

                
       
   

    