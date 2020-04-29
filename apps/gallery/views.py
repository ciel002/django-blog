from django.shortcuts import render


# Create your views here.
from utils.decorators import increase_web_visit
from utils.template import template_context


@increase_web_visit
def index_view(request):
    context = template_context(tag='gallery')
    return render(request, 'gallery.html', context)
