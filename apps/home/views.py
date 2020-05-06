from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_POST

from blog.models import Post
from gallery.models import Picture
from home.forms import ContactEmailForm
from home.models import Banner
from utils.decorators import increase_web_visit
from utils.email_util import send_contact_mail
from utils.template import template_context


@increase_web_visit
def index_view(request):
    sliders = Banner.objects.order_by("add_time").all()[:5:-1]
    posts = Post.objects.order_by("-add_time").all()[:4]
    pictures = Picture.objects.order_by("-add_time").all()[:8]
    context = template_context(tag='home', sliders=sliders, posts=posts, pictures=pictures)
    return render(request, 'index.html', context)


@increase_web_visit
def contact_view(request):
    context = template_context(tag='contact')
    return render(request, 'contact.html', context)


@increase_web_visit
@require_POST
def contact_send_mail_view(request):
    if request.method == 'POST':
        form = ContactEmailForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            status = send_contact_mail(nickname=data.get('nickname'), email=data.get('email'),
                                       message=data.get('message'))
            if status:
                return JsonResponse(data={'code': 200})
        else:
            return JsonResponse(data={'code': -12})


def map_view(request):
    return render(request, 'map.html')
