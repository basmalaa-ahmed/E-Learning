from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import login, logout # type: ignore
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm # type: ignore
from .forms import CustomLoginForm
from django.http import HttpResponse # type: ignore
from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from django.contrib.auth import authenticate # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.hashers import make_password # type: ignore
from rest_framework.authtoken.models import Token # type: ignore
from django.contrib.auth.views import LoginView # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Check for the presence of data
        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Verify user data
        user = authenticate(username=username, password=password)

        if user is not None:
            # If user data is correct, return token
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            # Identify the error cause
            if not User.objects.filter(username=username).exists():
                return Response({"error": "Username does not exist"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "Incorrect password"}, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new user
        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password),  # Encrypt the password
        )
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

def index(request):
    x = {'name': 'AbdAllah Saad Mahmoud Ahmed', 'age': ''}
    return render(request, 'pages/index.html', x)

def about(request):
    return render(request, 'pages/about.html')

def courses(request):
    return render(request, 'courses/course_list.html')

def contact(request):
    return render(request, 'parts/contact.html')

def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request=request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Redirect to home or dashboard
    else:
        form = CustomLoginForm()

    return render(request, 'pages/index.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user
            return redirect('index')  # Replace 'home' with your desired URL name
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
