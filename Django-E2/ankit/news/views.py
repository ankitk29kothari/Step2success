from django.shortcuts import render,HttpResponse
from .models import employee_details


# Create your views here.
def about(request):
	return render(request,'about.html',{news=employee_details.objects.all()})


def home(request):
    return render(request,'home.html')
    #return HttpResponse("Hello, world. You're at the home index.")