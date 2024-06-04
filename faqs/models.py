from django.db import models


class Title(models.Model):
    name = models.CharField(max_length=155, help_text='Title of question')

    class Meta:
        verbose_name_plural = 'Titles'

    def __str__(self) -> str:
        return self.name


class Asked(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, help_text='Title of question')
    question = models.CharField(max_length=255, help_text='Question')
    answer = models.TextField(max_length=50000, help_text='Answer')
    posted = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Asked'

    def __str__(self) -> str:
        return self.question
