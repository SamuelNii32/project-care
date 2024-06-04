import time
from itertools import chain

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages

from contacts.models import Subscriber
from projects.models import Topic, Department
from faqs.models import Title, Asked
from utils import helper


def home(request):
    if request.method == 'POST':
        email = request.POST['email']

        if email:
            subscribed_email = Subscriber.objects.filter(email=email).first()

            if subscribed_email:
                date_joined = subscribed_email.joined
                messages.success(request, f"You have already subscribed to our newsletters.")
            else:
                Subscriber.objects.create(email=email)
                messages.success(request, "Thank you for subscribing to our Newsletters! You'll receive updates in your email if it's valid.")

        return redirect(home)

    context = {
        'page': 'home',
        'project_topics': Topic.objects.all().count(),
        'departments': Department.objects.all().count()
    }
    
    # if helper.refresh_data():
    #     return refresh_content(request)
        
    return render(request, 'core/pages/home.dj', context)


def faq(request):
    titles = Title.objects.all()
    asked = Asked.objects.all()

    def last_modified():
        date = asked.last().posted.strftime("%d %b, %Y")

    context = {
        'page': 'faq',
        'titles': titles,
        'asked': asked,
        'last_modified': asked.last().posted.strftime("%d %b, %Y %H:%M %p") if asked else ''
    }
    
    # if helper.refresh_data():
    #     return refresh_content(request)
        
    return render(request, 'core/pages/faq.dj', context)


def terms(request):
    context = {
        'page': 'terms',
    }
    
    # if helper.refresh_data():
    #     return refresh_content(request)
        
    return render(request, 'core/pages/terms.dj', context)
    

def refresh_content(request):
    context = {}
    return render(request, "core/pages/refresh.dj", context)
    

def search(request):
    try:
        q = request.GET['q']
    except:
        q = None

    if q:
        start = time.monotonic()

        result = None
        for word in q.split():
            query = Topic.objects.filter(title__icontains=word)
            if result:
                result = list(chain(result, query))
            else:
                result = Topic.objects.filter(title__icontains=word)
        try:
            page = request.GET['page']
        except:
            page = 1

        paginator = Paginator(result, per_page=50)
        page_object = paginator.get_page(page)
        page_object.adjusted_elided_pages = paginator.get_elided_page_range(page)
        
        duration = time.monotonic() - start

    departments = Department.objects.all()

    context = {
        'page': 'search',
        'departments': departments,
        'page_obj': page_object,
        'count': paginator.count,
        'duration': "{:.2f}".format(duration),
        'q': q,
    }
    
    # if helper.refresh_data():
    #     return refresh_content(request)
        
    return render(request, "core/pages/search.dj", context)

