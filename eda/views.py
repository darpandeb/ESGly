from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    '''if request.user.is_superuser:
        return render(request,'index.html',context={})
    else:
        return render(request,'pages-error-404.html',{})'''

    return render(request, 'index.html', context={})



def gentab(request):
    return render(request, 'tables-general.html', context={})


def datatab(request):
    return render(request, 'tables-data.html', context={})

def pharma(request):
    return render(request, 'pharma.html', context={})


def globaltab(request):
    return render(request, 'charts-apexcharts.html', context={})


def indiatab(request):
    return render(request, 'charts-chartjs.html', context={})


def chinatab(request):
    return render(request, 'charts-echarts.html', context={})


def contact(request):
    return render(request, 'pages-contact.html', context={})


def profile(request):
    return render(request, 'users-profile.html', context={})

def sentiments(request):
    return render(request, 'sentiments.html', context={})