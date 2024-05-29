
from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from .forms import JobForm
from .forms import JobApplicationForm
from django.contrib.auth.decorators import login_required
from .models import Job, JobApplication

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'job_detail.html', {'job': job})

def job_create(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'job_form.html', {'form': form})

def job_update(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm(instance=job)
    return render(request, 'job_form.html', {'form': form})

def job_delete(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        job.delete()
        return redirect('job_list')
    return render(request, 'job_confirm_delete.html', {'job': job})


def homepage(request):
    jobs=Job.objects.all()
    context={'jobs':jobs}
    return render(request,'homepage.html',context)

@login_required
def apply_to_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            return redirect('job_list')  # Redirect to home page after applying
    else:
        form = JobApplicationForm()
    return render(request, 'apply_to_job.html', {'form': form, 'job': job})