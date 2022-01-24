from django.shortcuts import render

# Create your views here.
def header_view(request,**kwargs):
    return render(request,"header.html")