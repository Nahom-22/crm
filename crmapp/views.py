from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def dashboard(request):
    #return render(request,'crmapp/dashboard.html')
     return(HttpResponse('Dashboard'))
def customers(request):
    #return render(request,'crmapp/customers.html')
    return(HttpResponse('customers'))
def register(request):
    #return render(request, 'crmapp/register.html')
    return(HttpResponse('Register'))
def login(request):
    return render(request,'crmapp/login.html')

def home(request):
    return render(request,'crmapp/index.html')