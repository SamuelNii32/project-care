from django.contrib import admin
from django.db import models
from taggit.managers import TaggableManager


def project_file(instance, filename):
    return '/'.join(['files', 'projects', '', filename])


class Department(models.Model):
    name = models.CharField(max_length=155, default=None, help_text='Department name')
    image_id = models.CharField('Image ID', max_length=15, default=None, help_text='Unsplash image ID')

    class Meta:
        verbose_name_plural = 'Departments'

    def __str__(self) -> str:
        return self.name.__str__()


class Topic(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, help_text='Project topic department')
    title = models.CharField(max_length=555, default=None, help_text='Topic title')
    brief = models.TextField(max_length=100000, null=True, blank=True, help_text='Project Brief')
    file = models.FileField(upload_to=project_file, null=True, blank=True, help_text='Project file')
    pages = models.IntegerField(help_text='Number of pages')
    price = models.CharField(max_length=55, help_text='Project price')
    chapters = models.CharField(max_length=55, help_text='Number of chapters')
    extension = models.CharField(max_length=60, null=True, blank=True, default="", help_text="Format")
    tags = TaggableManager(help_text='Related names to other projects')

    class Meta:
        verbose_name_plural = 'Topics'
        ordering = ['title']
        
    def __str__(self) -> str:
        return self.title.__str__()
        

class TopicAdmin(admin.ModelAdmin):
    search_fields = ['title',]


class Transaction(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING, help_text='Project topic')
    first_name = models.CharField(max_length=60, default=None, help_text='First name')
    last_name = models.CharField(max_length=60, default=None, help_text='Last name')
    email = models.EmailField(help_text='Email')
    phone = models.CharField(max_length=255, default=None, help_text='Phone number')
    paid = models.CharField(max_length=60, default="0.00", help_text='Amount paid')
    where_heard = models.CharField(max_length=255, default=None, help_text='Where the person heard about Project Care', blank=True, null=True)
    referrer_phone = models.CharField(max_length=255, default=None, help_text='Referrer phone number', blank=True, null=True)
    reference = models.CharField(max_length=255, default='', help_text='Transaction reference')
    occurred = models.DateTimeField(auto_now=True, help_text='Date of transaction')
    settled = models.BooleanField(default=False, help_text='Files has been sent')

    class Meta:
        verbose_name_plural = 'Transactions'

    def __str__(self) -> str:
        return f'{self.reference.__str__()} | {self.email.__str__()} | {self.occurred.date().__str__()} {self.occurred.time().__str__()[:5]}'


class Paystack(models.Model):
    public_key = models.CharField(max_length=500, default=None, blank=True, null=True)
    secret_key = models.CharField(max_length=500, default=None, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Paystack'
    
    def __str__(self) -> str:
        return str(self.public_key)
