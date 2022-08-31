from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>Hello Django!<h1/></b> <a href='/listings'>Visit Listings </a>")

def about(request):
    return HttpResponse("<h1>About Us!<h1/></b> <a href='/contact'>Visit Contact </a>")

def contact(request):
    return HttpResponse("<h1>Contact page</h1></b> <a href='/hello'>Visit Home </a>")

def listings(request):
    return HttpResponse("<h1>Hello Lists!<h1/></b> <a href='/about-us'>Visit About us </a>")