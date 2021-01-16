from django.shortcuts import render
from courses.models import Course, Major, Achievment


def major_detail(request, pk):
    major = Major.objects.get(pk=pk)
    context = {
        'major': major
    }
    return render(request, 'major_detail.html', context)


def major_index(request):
    majors = Major.objects.all()
    context = {
        'majors': majors
    }
    return render(request, 'major_index.html', context)
