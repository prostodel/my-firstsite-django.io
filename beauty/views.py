from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Course

def index(request):
    courses = Course.objects.all()
    return render(request, 'beauty/courses.html',{'courses':courses})

def single_course(request, course_id):
    # option1
    # try:
    #     course = Course.objects.get(pk=course_id)
    #     return render(request, 'single_course.html', {'course': course})
    # except Course.DoesNotExist:
    #     raise Http404()
    # return HttpResponse(''.join([str(course) +'<br>' for course in courses]))

    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'beauty/single_course.html', {'course': course})
