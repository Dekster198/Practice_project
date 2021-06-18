from django import http
from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

def index(request):
    return render(request, 'index.html')

def price(request, name, price):
    output = '<h2>Название товара: {0} <br> Цена: {1}</h2>'.format(name, price)
    return HttpResponse(output)

def products(request, productid):
    category = request.GET.get('cat', '')
    output = '<h2>Product <br> id: {0} <br> category: {1}'.format(productid, category)
    return HttpResponse(output)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1 align="center">Страница не найдена</h1>')
