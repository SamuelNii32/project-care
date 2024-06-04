
from django import template

from projects.models import Topic


register = template.Library()

@register.filter
def format_path(value):
    return value.lower().replace('-', 'symedashsign').replace('/', 'symeorsign').replace(' ', '-')


@register.filter
def count_topics(department):
    return Topic.objects.filter(department=department).count()


@register.filter
def trancate(topic, length):
    return (topic[:length] + '..') if len(topic) > length else topic

