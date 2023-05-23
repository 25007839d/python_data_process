from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from adwait_solution.customer.models import Customer
from adwait_solution.customer.serialozers import CustomerModelSerializer

# Create your views here.
class CustomerAPIView(APIView):
    def get(self,request,*args,**kwargs):
        colors = ['red','blue','green']
        return Response({'msg':'dush','colors':colors})


class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class = CustomerModelSerializer()

