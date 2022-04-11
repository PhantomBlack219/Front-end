from multiprocessing import context
from re import template
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.detail import DetailView

from .models import Owasp, Aindice
# Create your views here.
#index
def index(request):
    listaO = Owasp.objects.all()
    context = {'listaO':listaO}
    template = loader.get_template('home/index.html')
    return HttpResponse(template.render(context,request))
#vista para ver Owasp
def verOwasp(request, id):
    listaA = Aindice.objects.all()
    context = {'listaA':listaA}
    context['object'] = Owasp.objects.get(id = id)

    return render(request,'others/owasp.html',context)
#vista para ver paginas hint, log y data
def hints(request):
    template = loader.get_template('others/hints.html')
    context = {}
    return HttpResponse(template.render(context,request))

def log(request):
    template = loader.get_template('others/log.html')
    context = {}
    return HttpResponse(template.render(context,request))

def data(request):
    template = loader.get_template('others/data.html')
    context = {}
    return HttpResponse(template.render(context,request))