from django.shortcuts import render, get_object_or_404
from feed.models import Post
from .models import EduProgram


def edu_list(request):
    programs = EduProgram.objects.all()
    posts = Post.objects.order_by('-timestamp')[:3]
    context = {
        'programs': programs,
        'posts': posts
    }
    return render(request, 'education/index.html', context=context)


def program_detail(request, slug):
    program = get_object_or_404(EduProgram, slug__iexact=slug)
    context = {
        'program': program,
    }
    return render(request, 'education/program_detail.html', context=context)
