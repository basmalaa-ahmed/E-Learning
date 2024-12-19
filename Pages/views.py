from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .forms import CustomLoginForm
from django.http import HttpResponse # type: ignore


# Create your views here.
def index (request):
    # return HttpResponse('AAAAAAAAAAAAAAAA')
    x={'name':'AbdAllah Saad Mahmoud Ahmed','age': ''}
    # username = request.user.username

    return  render(request,'pages/index.html', x)

def about (request):
    return  render(request,'pages/about.html')
def courses (request):
    return  render(request,'parts/courses.html')
def contact (request):
    return  render(request,'parts/contact.html')


def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request=request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Redirect to home or dashboard
    else:
        form = CustomLoginForm()

    return render(request, 'pages/index.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('index')

# def logout_view(request):
#     logout(request)
#     return redirect('index')  # Replace 'home' with your desired redirect URL name




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
