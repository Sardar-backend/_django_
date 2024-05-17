from django.shortcuts import render

from django.http import HttpResponse

def http_test(request):
     return render(request,'Templates/about.html')
def http_about(request):
     return render(request,'Templates/index.html')
