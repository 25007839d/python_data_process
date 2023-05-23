from django.contrib import admin
from .models import emp

@admin.register(emp)
class EmpAdmin(admin.ModelAdmin):
    list_display = ['name','eid','city','dept']

# Register your models here.
