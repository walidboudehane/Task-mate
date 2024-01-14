from django.shortcuts import render
from django.http import HttpResponse

def todolist(request):
    context = {'welcome_todolist':'welcome to taskmate !'}
    return render(request,'todolist.html',context)
def contact(request):
    context = {'welcome_contact':'welcome to contact !'}
    return render(request,'contact.html',context)
def about(request):
    context = {'welcome_about':'welcome to about !'}
    return render(request,'about.html',context)