from markdown import markdown
from django.shortcuts import render

# Create your views here.
from blog.models import Post, Category
from utils.decorators import increase_web_visit
from utils.pagination import pagination
from utils.template import template_context


@increase_web_visit
def index_view(request, page=1, category_name=''):
    categories = Category.objects.filter(post__category__isnull=False).distinct().all()
    keyword = request.GET.get('s', '')

    if category_name == '' and keyword == '':
        posts = Post.objects.order_by("-add_time").all()
    elif category_name == '' and keyword != '':
        posts = Post.objects.filter(title__icontains=keyword).order_by("-add_time").all()
    elif category_name != '' and keyword == '':
        posts = Post.objects.filter(category__sub_name=category_name).order_by("-add_time").all()
    else:
        posts = Post.objects.filter(category__sub_name=category_name, title__contains=keyword).order_by(
            "-add_time").all()
    pages, page_range = pagination(page=page, queryset=posts, per_page=5)

    context = template_context(tag='blog', pages=pages, page_range=page_range, categories=categories, category_name=category_name)
    return render(request, 'blog.html', context)


@increase_web_visit
def search_view(request, page=1):
    categories = Category.objects.filter(post__category__isnull=False).distinct().all()

    keyword = request.GET.get('keyword')
    posts = Post.objects.filter(title__contains=keyword).all()

    pages, page_range = pagination(page=page, queryset=posts, per_page=5)
    context = template_context(tag='blog', pages=pages, page_range=page_range, categories=categories)
    return render(request, 'blog.html', context)


@increase_web_visit
def post_view(request, title):
    post = Post.objects.filter(title=title).first()
    # 访问量加1
    post.increase_click_num()
    post.content = markdown(post.content,
                            extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite',
                                        'markdown.extensions.toc'])
    context = template_context(tag='blog', post=post)
    return render(request, 'post.html', context=context)
