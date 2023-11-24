from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requset):
    return HttpResponse("Onememos")
def createMemo(request):
    return HttpResponse("Create Memo")