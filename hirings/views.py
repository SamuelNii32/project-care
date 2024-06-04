from django.shortcuts import render, redirect
from django.contrib import messages

from contacts.models import Hiring


def hire_writer(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        project_title = request.POST['projectTitle']
        education_level = request.POST['educationLevel']
        department = request.POST['department']

        hiring = Hiring.objects.create(fullname=fullname, email=email, phone=phone, project_title=project_title, education_level=education_level)
        
        if department:
            hiring.department = department
            hiring.save()

        messages.success(request, "We have recieved your request. A support member will get back to you shortly.")
        return redirect(hire_writer)

    context = {
        'page': 'hire-writer',
    }
    return render(request, 'core/pages/hire-writer.dj', context)
