from django.shortcuts import render


# Create your views here.
from gallery.models import Picture
from utils.decorators import increase_web_visit
from utils.pagination import pagination
from utils.template import template_context


@increase_web_visit
def index_view(request, page=1):
    pictures = Picture.objects.order_by('-add_time').all()
    pages, page_range = pagination(page=page, queryset=pictures, per_page=16)
    context = template_context(tag='gallery', pages=pages, page_range=page_range)
    return render(request, 'gallery.html', context)
