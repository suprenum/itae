from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Post, Tag
from .forms import PostForm, TagForm
from .utils import ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin


def paginate(request, queryset):
    paginator = Paginator(queryset, 3)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    context = {
        'page': page,
        'is_paginated': is_paginated,
    }
    return context


def search_view(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    search_query = request.GET.get('q')

    if search_query:
        posts = Post.objects.filter(
            Q(title__icontains=search_query) | Q(content__icontains=search_query))

    context = {
        'posts': posts,
        'tags': tags,
        'search_query': search_query
    }
    paginator_context = paginate(request, posts)
    context.update(paginator_context)

    return render(request, 'feed/search_results.html', context=context)


def news_list(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()

    context = {
        'tags': tags,
    }
    paginator_context = paginate(request, posts)
    context.update(paginator_context)
    return render(request, 'feed/index.html', context=context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug__iexact=slug)

    context = {
        'post': post,
        'admin_object': post,
        'detail': True
    }
    return render(request, 'feed/post_detail.html', context=context)


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = PostForm
    template = 'feed/post_create_form.html'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'feed/post_update_form.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'feed/post_delete_form.html'
    redirect_url = 'news_list_url'
    raise_exception = True


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    tags = Tag.objects.all()

    context = {
        'tag': tag,
        'tags': tags,
        'admin_object': tag,
        'detail': True
    }
    paginator_context = paginate(request, tag.posts.all())
    context.update(paginator_context)
    return render(request, 'feed/tag_detail.html', context=context)


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = TagForm
    template = 'feed/tag_create_form.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'feed/tag_update_form.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'feed/tag_delete_form.html'
    redirect_url = 'news_list_url'
    raise_exception = True
