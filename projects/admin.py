from django.contrib import admin

from projects.models import Paystack, Department, Topic, Transaction, TopicAdmin

admin.site.register(Paystack)
admin.site.register(Department)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Transaction)
