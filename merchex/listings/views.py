from optparse import TitledHelpFormatter
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Band, Title

def hello(request):
    bands =Band.objects.all()
    title = Title.objects.all()
    return HttpResponse(f"""<h1>Hello Django!<h1/></b> <a href='/listings'>Visit Listings </a></b>
    <p>My favorurite bands:</p></b>
    <ul>
        <li>{bands[0].name}</li>
        <li>{bands[1].name}</li>
        <li>{bands[2].name}</li></b>
        <p>My favourite titles:</p>
        <li>{title[0].name}</li>
        <li>{title[1].name}</li>
        <li>{title[2].name}</li>
    </ul>""")

def about(request):
    return HttpResponse("<h1>About Us!<h1/></b> <a href='/contact'>Visit Contact </a>")

def contact(request):
    return HttpResponse("<h1>Contact page</h1></b> <a href='/hello'>Visit Home </a>")

def listings(request):
    return HttpResponse("<h1>Hello Lists!<h1/></b> <a href='/about-us'>Visit About us </a>")