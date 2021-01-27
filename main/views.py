from django.shortcuts import render
from feed.models import Post
from staff.models import Member


def index(request):
    posts = Post.objects.order_by('-timestamp')[:3]
    member = Member.objects.all()[:1].get()

    context = {
        'posts': posts,
        'member': member,
    }
    return render(request, 'main/index.html', context=context)
