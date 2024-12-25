from django.contrib.auth import views as auth_views # type: ignore
from django.urls import path # type: ignore
from . import views
from django.urls import path # type: ignore
from .views import  LoginView
from .views import  LoginView, RegisterView



# Define the urlpatterns
urlpatterns = [
    path('', views.index, name='index'),  
    path('about', views.about, name='about'),  
    path('courses',views.courses,name='courses'),
     path('contact',views.contact,name='contact'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', views.custom_logout, name='logout'),
    #  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('signup/', views.signup_view, name='signup'),
 path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),

]
