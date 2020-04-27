from project.models import YzbUniversityName
from django import template

register = template.Library()


def university_name(value):
    value = value[:5]
    try:
        name = YzbUniversityName.objects.values("name").filter(code=value).first().get('name')
    except:
        name = ''
    return name


register.filter('university_name', university_name)
