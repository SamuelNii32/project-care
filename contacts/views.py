from django.shortcuts import redirect, render
from django.contrib import messages

from .models import Message


def contact_us(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        try:
            attachment = request.FILES['attachment']
        except:
            attachment = None

        msg = Message.objects.create(fullname=fullname, email=email, phone=phone, message=message)
        
        if attachment:
            msg.attachment = attachment
            msg.save()

        messages.success(request, "Thanks for contacting us. A support member will get back to you shortly." )
        return redirect(contact_us)

    context = {
        'page': 'contact-us',
    }
    return render(request, 'core/pages/contact-us.dj', context)
