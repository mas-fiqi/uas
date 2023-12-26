from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def hom(request):
  template = loader.get_template('hom.html')
  return HttpResponse(template.render())
def comen(request):
  template = loader.get_template('comen.html')
  return HttpResponse(template.render())
def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
def work(request):
  template = loader.get_template('work.html')
  return HttpResponse(template.render())
def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())
def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())
def index1(request):
  template = loader.get_template('index1.html')
  return HttpResponse(template.render())
