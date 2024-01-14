from django.shortcuts import render
from django.http import HttpResponse

def todolist(request):
    return HttpResponse("Hello to task page")

