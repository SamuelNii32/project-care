from calendar import c
from traceback import StackSummary
from django.contrib import admin

from .models import Message, Hiring, Subscriber


admin.site.register(Message)
admin.site.register(Hiring)
admin.site.register(Subscriber)
