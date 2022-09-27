from optparse import TitledHelpFormatter
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Band, Title

def hello(request):
    bands =Band.objects.all()
    title = Title.objects.all()
    return render(request, 'listings/hello.html', {'Title': title,'bands':bands})

def about(request):
    bands = Band.objects.all()
    return render(request, 'listings/about.html')
    
def contact(request):
    return render(request, 'listings/contact.html')

def listings(request):
    return render(request, 'listings/listings.html')