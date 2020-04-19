from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
	return HttpResponse('<h1>ANKIT</h1>')



def about(request):
	return HttpResponse('<h1>About us</h1>')


def login(request):
	return HttpResponse('<h1>Login</h1>')