from django.shortcuts import render


# Create your views here.
from utils.template import template_context


def index_view(request):
    context = template_context(tag='gallery')
    return render(request, 'gallery.html', context)
