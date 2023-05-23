from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
def emp_info(request):

    data = [
        'ankit','dushyant'
    ]
    return JsonResponse(data,safe=False)

    # return HttpResponse(" Hi this id dushyant")

 # 9149273837 jaya
#8678960199 kishore

# tmmo forex fund
