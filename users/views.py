from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserLoginForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from jobs.models import Job

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('signup')
    else:
        form = CustomUserCreationForm()
        return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('job_list')
    else:
        form = CustomUserLoginForm()
        return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    if request.user.user_type == 'recruiter':
        jobs = Job.objects.filter(created_by=request.user)
        return render(request, 'users/recruiter_home.html', {'jobs': jobs})
    else:
        jobs = Job.objects.all()
        return render(request, 'users/applicant_home.html', {'jobs': jobs})

class JobCreateView(CreateView):
    model = Job
    fields = ['title', 'description', 'requirements']
    template_name = 'job_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class JobListView(ListView):
    model = Job
    template_name = 'job_list.html'

class JobDetailView(DetailView):
    model = Job
    template_name = 'job_detail.html'

class JobDeleteView(DeleteView):
    model = Job
    template_name = 'job_confirm_delete.html'
    success_url = reverse_lazy('home')


@login_required
def home(request):
    jobs = Job.objects.all()  # Fetch all job listings
    return render(request, 'users/home.html', {'jobs': jobs})