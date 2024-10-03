from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'crmapp/index.html')

def dashboard(request):
    return render(request,'crmapp/dashboard.html')

def customers(request):
    return render(request,'crmapp/customers.html')

def register(request):
    return render(request, 'crmapp/register.html')

def login(request):
    return render(request,'crmapp/login.html')