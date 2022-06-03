from django.shortcuts import render
from django.http import JsonResponse

from .CompanyData import *

# Create your views here.

def Company(request):

    return render(request,"Company/Company.html",{})

def getCompanyData(request):

    if request.method == "GET":

        result = request.GET

        if result:

            content_type = result.get('type','')

            if content_type == "Country" or content_type == "Sector":

                return JsonResponse(getPieChart(content_type), safe = False)

    return JsonResponse(getCompanies(), safe = False)

def Detail(request, Symbol):

    return render(request,"Company/Company.html",{})

def getCompanyDetail(request):

    if request.method == "GET":

        result = request.GET

        if result:

            Symbol = result.get('Symbol')

            return JsonResponse({'Info': getDetail(Symbol), 'Option': getStock(Symbol)})

    return JsonResponse({'Info': {}, 'Option': []})
