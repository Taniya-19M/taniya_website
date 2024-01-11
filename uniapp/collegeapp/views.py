
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm
from .models import CustomUser, FormData
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse
from .forms import FormDataForm
from django.http import HttpResponse



def logout_view(request):
    return redirect('home')

def contact_us_view(request):
    return render(request, 'contact_us.html')

def home_view(request):
    return render(request, 'home.html')

def about_us_view(request):
    return render(request, 'about_us.html')

def services_view(request):
    return render(request, 'services.html')


def dashboard_view(request):
    data = FormData.objects.all()
    return render(request, 'dashboard.html', {'data': data})





def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # login_url = reverse('login')
            # return redirect(login_url)
            return HttpResponse('Success') 
    else:
        form = SignUpForm()
        # return HttpResponse('failure') 
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            dashboard_url = reverse('home')
            return redirect(dashboard_url)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})




def form_view(request):
    if request.method == 'POST':
        form = FormDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the same view after successful form submission
    else:
        form = FormDataForm()

    data = FormData.objects.all()  # Fetch all form submissions
    return render(request, 'contact_us.html', {'form': form, 'data': data})
