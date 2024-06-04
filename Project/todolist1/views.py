

from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib.auth.models import User
from .models import Task
from .forms import TaskForm

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")
        
        if password != cpassword:
            messages.error(request, "Passwords do not match. Please retry.")
            return redirect("/signup")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("/signup")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("/signup")
        
        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.save()       
        return redirect("/login")
    
    else:
        messages.info(request, "Please sign up.")
        
    return render(request, "signup.html")


def handlelogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        myuser = authenticate(username=username, password=password)
        
        if myuser is not None:
            login(request, myuser)
            if myuser.is_superuser:  
                messages.success(request, 'login successful')
                return redirect('view_tasks')  
            else:
                messages.success(request, 'User login successful')
                return redirect('view_tasks') 
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
        
    return render(request, "login.html")


def logout(request):
    django_logout(request)
    return redirect('login')


def view_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'view_tasks.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_tasks')
    return redirect('view_tasks')

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('view_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('view_tasks')
    return redirect('view_tasks')