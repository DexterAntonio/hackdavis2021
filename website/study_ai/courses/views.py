from django.shortcuts import render
from courses.models import Course, Major, Achievment
from .major_add_form import CommentForm


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


def enter_data_form(request):
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_major = form.cleaned_data["major_title"]
            major_website = form.cleaned_data["major_website"]
            body = form.cleaned_data["body"]
            requirements = body.split(',')
            new_major = Major(name=new_major, webpage=major_website)
            new_major.save()
            all_achievements = Achievment.objects.all()
            
            for req in requirements:
                if not req in all_achievements: 
                    new_ach = Achievment(name='placeholder',
                                         requirements=req)
                    new_ach.save()
                    ach = new_ach
                else:
                    ach = Achievment.objects.filter(requirements=req)[0]
                    print(req)

                new_major.requirements.add(ach)
                         
            new_major.requirements.add()
    context = {
        'form': form
    }

    return render(request, "enter_form.html", context)

