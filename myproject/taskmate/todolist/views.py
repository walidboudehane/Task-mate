from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from  todolist.models import Task
from todolist.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required
def todolist(request):
    if request.method=="POST":
        form=TaskForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).manage=request.user
            form.save()
        
        messages.success(request,'new task added')
        return redirect('todolist')
    else:
        all_tasks=Task.objects.filter(manage=request.user)
        paginator=Paginator(all_tasks,per_page=7)
        page=request.GET.get('pg')
        all_tasks=paginator.get_page(page)
        return render(request,'todolist.html',{'all_tasks':all_tasks})
@login_required
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task.manage==request.user:
        task.delete()
    else:
        messages.error(request,'Access restricted , you are not allowed !')
        
    return redirect('todolist')

@login_required
def edit_task(request,task_id):
    if request.method=="POST":
        task=Task.objects.get(pk=task_id) 
        form=TaskForm(request.POST or None ,instance=task)
        if form.is_valid():
            form.save()  
        messages.success(request,'Task edited !')
        return redirect('todolist')    
    else:
        task_obj=Task.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj':task_obj})
    
@login_required
def complete_task(request,task_id):
    task = Task.objects.get(pk=task_id)
    if task.manage==request.user:
        task.done=True
        task.save()
    else:
        messages.error(request,'Access restricted , you are not allowed !')
        
    return redirect('todolist')

@login_required
def pending_task(request,task_id):
    task = Task.objects.get(pk=task_id)
    task.done=False
    task.save()
    return redirect('todolist')

def index(request):
    context = {'welcome_index':'welcome to index !'}
    return render(request,'index.html',context)
 
def contact(request):
    context = {'welcome_contact':'welcome to contact !'}
    return render(request,'contact.html',context)

def about(request):
    context = {'welcome_about':'welcome to about !'}
    return render(request,'about.html',context)