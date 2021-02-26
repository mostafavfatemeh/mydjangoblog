from django.shortcuts import render
from . import models

def articles_list(request):
    arti=models.Dastan.objects.all().order_by('date')
    args={'artii':arti}
    return render(request,'articc/artic_list.html',args)
