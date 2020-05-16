from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
from .models import posts

posts_dummy=[

	{'author':'Ankit Kothari',
		'tittle':'python',
		'content':'First post',
		'date_posted':'August 27,2018'

	},



	{'author':'Ankit Kothari',
		'tittle':'python2',
		'content':'Second post',
		'date_posted':'August 27,2018'

	},
	{'author':'Himanshu',
		'tittle':'python',
		'content':'Third post',
		'date_posted':'August 27,2018'

	}


]



title='Blog'


def home(request):
	context={'posts':posts,'title':title}
	return render(request,'home.html',{'posts':posts.objects.all(),'title':title})



def about(request):
	return render(request,'about.html',{'posts':posts.objects.all()})


def login(request):
	return render(request,'login.html')

