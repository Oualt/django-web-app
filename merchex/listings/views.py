from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Band

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', context={'bands': bands})

def about(request):
    return HttpResponse('<h1>About Us</h1> <p>Nous adorons Merch !</p>')