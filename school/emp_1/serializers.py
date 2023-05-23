from rest_framework import serializers
from .models import emp

class EmpSerilizer (serializers.Serializer):
    name = serializers.CharField(max_length=99)
    eid = serializers.IntegerField
    city = serializers.CharField(max_length=50)
    dept = serializers.CharField(max_length=30)

def create(self,validate_date):
    return emp.ob
