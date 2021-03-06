from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage

# Create your views here.
def home(request):
    return render(request, 'index.html')

def store(request):
    products = Product.objects.all()
    return render(request, 'store.html', {'products':products})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect('store.html')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("store.html")
            else:
                messages.info(request, "Please enter your username and password")
                return render(request, 'signin.html')
        else:
            return render(request, 'signin.html')

def signout(request):
    logout(request)
    return redirect('signin.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password1')
            password = request.POST.get('password2')


            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password1')
                password = form.cleaned_data.get('password2')
                user = authenticate(username=username, password=password)
                user.is_active = False

                email_subject = 'Activate your account'
                email_body = 'This is Drone'
                email = EmailMessage(
                    email_subject,
                    email_body,
                    'noreply@semicolon.com',
                    [email],
                    # ['bcc@example.com'],
                    # reply_to=['another@example.com'],
                    # headers={'Message-ID': 'foo'}
                )
                email.send(fail_silently=True)
                messages.success(request, "Account was created for " + username)
                login(request, user)
                return redirect("signin.html")
            else:
                return render(request, 'signup.html', {'form':form})
        else:
            form = CreateUserForm()
    return render(request, 'signup.html', {'form':form})