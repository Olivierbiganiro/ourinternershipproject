from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.http import HttpResponse,request

from nyamagabewebapp.models import services

def index(request):
    context = {
       'service':services.objects.all(),
       }
    return render(request, 'index.html', context)  

def detail_view(request, id):
    context ={}
    context["detail"] = services.objects.get(id = id)        
    return render(request, "detail.html", context)