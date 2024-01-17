from django.contrib import auth  # Import the auth module
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError



# Create your views here.
def login(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']

            # Use the auth.authenticate method to authenticate the user
            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)  # Log the user in
                return redirect('index')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')

        except MultiValueDictKeyError:
            messages.error(request, 'Missing required field(s)')
            return redirect('login')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            confirmpassword = request.POST['password1']

            if password == confirmpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username Taken")
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email Taken")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                    last_name=last_name, email=email)

                    user.save()
                    return redirect('login')

            else:
                messages.info(request, "Password not matching")
                return redirect('register')
        except MultiValueDictKeyError:
            messages.error(request, "Missing required field(s)")
            return redirect('register')

    # Provide a default rendering for the GET request
    district = ['ernakulam', 'kozhikode']
    branch = {
        'ernakulam': ['Aluva', 'Edapally', 'Angamaly', 'Other Branches'],
        'kozhikode': ['Kondotty', 'Ramanattukara', 'Mukkam', 'Thamarassery', 'Other Branches'],
        # Add other districts and branches as needed
    }

    return render(request, 'register.html', {'districts': district, 'branches': branch})


def logout(request):
    # Your logout logic (optional)
    return redirect('index')


def form(request):
    # Handle form logic
    return render(request, 'form.html')