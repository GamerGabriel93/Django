from django.shortcuts import render, redirect

from .models import Todo

# Create your views here.

def home(request):
    undone_jobs = Todo.objects.filter(done='False').values()
    done_jobs = Todo.objects.filter(done='True').values()
    return render(request,'home.html', {'undone_jobs':undone_jobs, 'done_jobs':done_jobs})

def about(request):
    return render(request, 'about.html')

def new_job(request):

    if request.method == "GET":
        return render(request, 'new_job.html')
    elif request.method == "POST":
        job = request.POST.get('job')
        deadline = request.POST.get('deadline')
        done = request.POST.get('done')

        teendo = Todo(job=job, deadline=deadline, done=False)
        teendo.save()
        return redirect('home')
    
    return render(request, "new_job.html")