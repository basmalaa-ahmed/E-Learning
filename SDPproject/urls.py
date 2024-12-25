"""
URL configuration for SDPproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.urls import path,include # type: ignore
from django.contrib.auth import views as auth_views  # type: ignore # Importing auth_views here
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
from django.urls import path # type: ignore
# from .views import LoginView, RegisterView  # type: ignore # تأكد من أنك تستخدم نفس المسار الذي يحتوي على الفيوهات



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Pages.urls')),
    # path('courses',include('courses.urls')),
    # path("polls/", include("pages.urls")),
    # path("polls/", include("polls.urls")),
    path('courses/',include('courses.urls')),

    # Login URL
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # Logout URL
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #  path('api/register/', RegisterView.as_view(), name='register'),
    # path('api/login/', LoginView.as_view(), name='login'),


]
if settings.DEBUG:  # Only serve media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # type: ignore
