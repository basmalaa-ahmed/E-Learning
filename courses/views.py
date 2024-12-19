# from django.shortcuts import render
# from .models import Course

# # Create your views here.
# def course(request):
#     return render(request,"courses/course.html",{'coursesx',course.objects.all()})
# def courses(request):
#     return render(request,"courses/courses.html",{'coursesx',courses.objects.all()}) 
from .forms import courseEntryForm


from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson, Enrollment
from django.contrib.auth.decorators import login_required

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

@login_required
def enroll_in_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    Enrollment.objects.get_or_create(user=request.user, course=course)
    return redirect('course_detail', pk=pk)



def courseEntry(request):
    if request.method == 'POST':
        form = courseEntryForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data into the database
            return redirect('entry_success')  # Redirect to a success page or any other page
    else:
        form = courseEntryForm()  # Show an empty form

    return render(request, 'courseEntry.html', {'form': form})

# views.py
def courseEntrysuccess(request):
    return render(request, 'courseEntrysuccess.html')
