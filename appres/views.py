from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    text = "<h1>Borys Kret blog</h1>"

    return HttpResponse(text)