from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from customer.models import Customer


class CustomerSerializer(serializers.Serializer):
    cno = serializers.IntegerField()
    cname = serializers.CharField(max_length=100)
    cmobile = serializers.IntegerField()
    cemail = serializers.EmailField()
    cbankname = serializers.CharField(max_length=30)
    caccountnumber = serializers.IntegerField()
    caccountifsccode = serializers.CharField(max_length=9)


class CustomerModelSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields= '__all__'
