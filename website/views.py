from django.shortcuts import render


def http_test(request):
     return render(request,'Templates/index.html')
def http_about(request):
     return render(request,'Templates/about.html')
def http_contact(request):
     return render(request,'Templates/contact.html')
