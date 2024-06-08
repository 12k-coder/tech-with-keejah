#from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
   # return HttpResponse ("hello ")
   return render(request, 'home.html')
def about(request):
  #  return HttpResponse("my abuot page.")
  return render(request, 'about.html')
def melvin(request):
  return render(request, 'melvin.html')