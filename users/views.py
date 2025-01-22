# users/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login as django_login
from .forms import UserRegisterForm
from .models import User
from django.utils.timezone import now

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Save the user instance, hashing the password
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()

            messages.success(request, "Signup successful! Please log in.")
            return redirect('login')
        else:
            messages.error(request, "There was an error with your signup. Please try again.")
    else:
        form = UserRegisterForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid email or password'})

        if check_password(password, user.password):
            # Update the last_login field
            user.last_login = now()
            user.save()

            # Log the user in
            django_login(request, user)

            # Redirect to the index page
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})

    return render(request, 'login.html')


def index_view(request):
    # Display the logged-in user's name
    user_name = request.user.name if request.user.is_authenticated else None
    return render(request, 'index.html', {'user_name': user_name})
