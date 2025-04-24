from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import tasks
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

def index(request):
    return redirect('/todo/')

def signUp(request):
    if request.method=="POST":
        user=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        my_user=User.objects.create_user(user,email,password)
        my_user.save()
        return redirect('/login')
    return render(request,'signUp.html')

def logIn(request):
    if request.method == "POST":
        user=request.POST.get('username')
        password=request.POST.get('password')
        userr=authenticate(request,username=user,password=password)
        if(userr is not None):
            login(request,userr)
            return redirect('/todo/')
        else:
            return redirect('/login/')
    return render(request, 'logIn.html')

def todos(request):
    if not request.user.is_authenticated:
        return redirect('/login/')  # replace with your login URL
    if request.method == "POST":
        if 'delete_task' in request.POST:
            # Handle delete action
            task_id = request.POST.get('delete_task')
            tasks.objects.filter(srno=task_id, user=request.user).delete()
            return redirect('/todo/')
        else:
            # Handle create action
            user = request.user.username
            name = request.POST.get('name')
            date = timezone.now().date()
            tasks.objects.create(user=request.user, name=name, date=date)
            return redirect('/todo/')
    
    works = tasks.objects.filter(user=request.user)
    return render(request, 'todo.html', {'tasks': works})

