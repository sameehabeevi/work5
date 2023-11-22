from django.http import HttpResponse
from django.shortcuts import render
from .models import place,person

# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj2=person.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj2})
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     Add=x+y;Sub=x-y;Mul=x*y;Div=x/y
#     return render(request,'result.html',{'add':Add,'sub':Sub,'mul':Mul,'div':Div})


