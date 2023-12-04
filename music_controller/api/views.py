from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# here has to be the endpoints

def main(request):
    return HttpResponse("<h1>Hello</h1>")
