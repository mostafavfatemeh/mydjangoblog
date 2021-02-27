from django.shortcuts import render,HttpResponse
from . import models

def articles_list(request):
    arti=models.Dastan.objects.all().order_by('-date')
    args={'artii':arti}
    return render(request,'articc/artic_list.html',args)

def artic_detail(request,slugg):
    dast=models.Dastan.objects.get(slug=slugg)
    return render(request,'articc/dastan_list.html',{'das':dast})