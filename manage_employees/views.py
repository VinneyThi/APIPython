from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.




def employee(request):
    context = {"testes":"foi"}
    print('testes {context}')
    return JsonResponse(context)
