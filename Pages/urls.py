from django.contrib.auth import views as auth_views # type: ignore
from django.urls import path # type: ignore
from . import views

# Define the urlpatterns
urlpatterns = [
    path('', views.index, name='index'),  # Replace 'home' with your view function
    path('about', views.about, name='about'),  # Replace 'home' with your view function
    # path('login/', views.custom_login, name='login'),
    path('courses',views.courses,name='courses'),
     path('contact',views.contact,name='contact'),
    # path('', views.home, name='home'),
    # path('logout/', views.custom_logout, name='logout'),
    # path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', views.custom_logout, name='logout'),
    path('signup/', views.signup_view, name='signup'),  # Define a URL pattern with name='signup'


]
