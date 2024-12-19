from django.urls import path
from . import views

# Define the urlpatterns
urlpatterns = [
    # path('', views.courses, name='courses'),  
    # path('course', views.course, name='course'),  
    
    path('', views.course_list, name='course_list'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
    path('<int:pk>/enroll/', views.enroll_in_course, name='enroll_in_course'),
    
    path('entry/', views.courseEntry, name='courseEntry'),
    path('success/', views.courseEntrysuccess, name='courseEntrysuccess'),

]
