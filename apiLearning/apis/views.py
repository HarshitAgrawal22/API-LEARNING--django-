from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from apis.models import company, employee
from apis.serializers import company_serializers, employee_serializers
from rest_framework.decorators import action
from rest_framework.response import Response

class comapanyViewSet(viewsets.ModelViewSet):
     queryset=company.objects.all()
     serializer_class=company_serializers
     
     
     @action(detail=True,methods=['get'])
     def employees(self,request,pk=None):# here name of the function defines the url 
          
          try:
               selected_company=company.objects.get(id=pk)
               current_Employee=employee.objects.filter(company=selected_company)
               company_employee=employee_serializers(current_Employee,many=True,context={'request':request})
               return Response(company_employee.data)
               #here pk is the primary key 
          except Exception as e :
               return Response({"message":"the company does'nt exists"})
          
class employeeViewSet(viewsets.ModelViewSet):
    queryset=employee.objects.all()#we can also order by means we can order it by our self 
    
    serializer_class=employee_serializers