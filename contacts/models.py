from django.db import models


def contact_files(instance, filename):
    return '/'.join(['files', 'contacts', '', filename])


class Message(models.Model):
    fullname = models.CharField(max_length=255, help_text='Fullname')
    email = models.EmailField(help_text='Email')
    phone = models.CharField(max_length=20, help_text='Phone number')
    message = models.TextField(max_length=50000, blank=True, null=True, help_text='Message')
    attachment = models.FileField(upload_to=contact_files, blank=True, null=True, help_text='Additional file')
    received = models.DateTimeField(auto_now_add=True, help_text='Date message was received')
    attended = models.BooleanField(default=False, help_text='Attended status')

    class Meta:
        verbose_name_plural = 'Messages'

    def is_attended(self):
        return '(Attended)' if self.attended else '(Not Attended)'

    def __str__(self) -> str:
        return f'{self.fullname.__str__()} | {self.received.date().__str__()} {self.received.time().__str__()[:5]} - {self.is_attended()}'


class Hiring(models.Model):
    fullname = models.CharField(max_length=255, help_text='Fullname')
    email = models.EmailField(help_text='Email')
    phone = models.CharField(max_length=20, help_text='Phone number')
    project_title = models.CharField(max_length=255, help_text='Project title')
    education_level = models.CharField(max_length=50, help_text='Education level')
    department = models.CharField(max_length=255, blank=True, null=True, help_text='Department/Project format')
    received = models.DateTimeField(auto_now_add=True, help_text='Date request was received')
    attended = models.BooleanField(default=False, help_text='Attended status')

    class Meta:
        verbose_name_plural = 'Hirings'

    def is_attended(self):
        return '(Attended)' if self.attended else '(Not Attended)'

    def __str__(self) -> str:
        return f'{self.fullname.__str__()} | {self.received.date().__str__()} {self.received.time().__str__()[:5]} - {self.is_attended()}'


class Subscriber(models.Model):
    email = models.EmailField(help_text='Subscriber email')
    joined = models.DateTimeField(auto_now_add=True, help_text='Subscribed date')

    class Meta:
        verbose_name_plural = 'Subscribers'

    def __str__(self) -> str:
        return f'{self.email.__str__()}'
