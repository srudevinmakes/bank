from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from bankapp.models import branches



# Create your views here.
def index(request):
    return render(request, 'base.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Basic validation: Check if username and password are provided
        if not username or not password:
            messages.error(request, 'Both username and password are required.')
            return render(request, 'login.html')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        # Check if the user is authenticated
        if user is not None:
            # Check if the user account is active (optional)
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Account is not active. Please contact support.')
        else:
            # Check if the error is due to incorrect username or password
            user_exists = User.objects.filter(username=username).exists()
            if user_exists:
                messages.error(request, 'Incorrect password')
            else:
                messages.error(request, 'Incorrect Username')

    return render(request, 'login.html')


def about(request):
    # Your view logic here
    return render(request, 'about.html')


def contact(request):
    # Your view logic here
    return render(request, 'contact.html')

#