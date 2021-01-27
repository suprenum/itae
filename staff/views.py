from django.shortcuts import render, get_object_or_404
from .models import Member, Tag
from feed.views import paginate


def members_list(request):
    members = Member.objects.all()
    tags = Tag.objects.all()

    context = {
        'tags': tags,
    }
    paginator_context = paginate(request, members)
    context.update(paginator_context)
    return render(request, 'staff/index.html', context=context)


def member_detail(request, slug):
    member = get_object_or_404(Member, slug__iexact=slug)

    context = {
        'member': member,
    }
    return render(request, 'staff/member_detail.html', context=context)


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    tags = Tag.objects.all()

    context = {
        'tag': tag,
        'tags': tags,
    }
    paginator_context = paginate(request, tag.members.all())
    context.update(paginator_context)
    return render(request, 'staff/tag_detail.html', context=context)
