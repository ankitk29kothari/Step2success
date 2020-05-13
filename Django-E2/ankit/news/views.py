from django.shortcuts import render,HttpResponse

# Create your views here.
def about(request):
	return render(request,'about.html')


def home(request):
    return HttpResponse("Hello, world. You're at the home index.")