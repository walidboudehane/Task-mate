from django.shortcuts import render,redirect
from django.http import HttpResponse
from  todolist.models import Task
from todolist.forms import TaskForm
from django.contrib import messages
def todolist(request):
    if request.method=="POST":
        form=TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,'new task added')
        return redirect('todolist')
    else:
        all_tasks=Task.objects.all()
        return render(request,'todolist.html',{'all_tasks':all_tasks})
def contact(request):
    context = {'welcome_contact':'welcome to contact !'}
    return render(request,'contact.html',context)
def about(request):
    context = {'welcome_about':'welcome to about !'}
    return render(request,'about.html',context)